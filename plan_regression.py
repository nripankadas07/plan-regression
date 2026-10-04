import argparse,json,math
from pathlib import Path
def load(path):
    x=json.loads(Path(path).read_text())
    if isinstance(x,list):
        if len(x)!=1:raise ValueError('expected one EXPLAIN statement')
        x=x[0]
    if not isinstance(x,dict) or not isinstance(x.get('Plan'),dict):raise ValueError('expected EXPLAIN JSON with Plan')
    return x['Plan']
def flatten(plan):
    result={};stack=[('root',plan)];count=0
    while stack:
        path,node=stack.pop();count+=1
        if count>10000:raise ValueError('plan exceeds 10000 nodes')
        if not isinstance(node,dict) or not isinstance(node.get('Node Type'),str):raise ValueError('invalid plan node')
        metrics={}
        for field in ('Total Cost','Plan Rows','Actual Total Time','Actual Rows','Actual Loops'):
            if field in node:
                v=node[field]
                if isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v) or v<0:raise ValueError(f'invalid {field}')
                metrics[field]=v
        result[path]={'identity':{k:node[k] for k in ('Node Type','Relation Name','Index Name','Join Type') if k in node},'metrics':metrics}
        children=node.get('Plans',[])
        if not isinstance(children,list):raise ValueError('Plans must be a list')
        for i,n in reversed(list(enumerate(children))):stack.append((f'{path}/{i}',n))
    return result
def compare(before,after,max_ratio=1.2,minimum_delta=0):
    if not math.isfinite(max_ratio) or max_ratio<1 or not math.isfinite(minimum_delta) or minimum_delta<0:raise ValueError('ratio must be >=1 and delta >=0')
    a,b=flatten(before),flatten(after);changes=[];regressions=[]
    for path in sorted(set(a)|set(b)):
        if path not in a or path not in b or a[path]['identity']!=b[path]['identity']:
            changes.append({'path':path,'before':a.get(path,{}).get('identity'),'after':b.get(path,{}).get('identity')});continue
        for field,old in a[path]['metrics'].items():
            if field not in b[path]['metrics']:continue
            new=b[path]['metrics'][field]
            if new>old*max_ratio and new-old>minimum_delta:
                regressions.append({'path':path,'metric':field,'before':old,'after':new,'ratio':new/old if old else None})
    return {'structural_changes':changes,'regressions':regressions,'baseline_nodes':len(a),'candidate_nodes':len(b),'matching':'positional paths with exact operator identity; changed operators are not numerically matched'}
def main():
    p=argparse.ArgumentParser();p.add_argument('before');p.add_argument('after');p.add_argument('--max-ratio',type=float,default=1.2);p.add_argument('--minimum-delta',type=float,default=0);a=p.parse_args()
    try:r=compare(load(a.before),load(a.after),a.max_ratio,a.minimum_delta)
    except (ValueError,OSError,RecursionError) as e:p.exit(2,str(e)+'\n')
    print(json.dumps(r,indent=2,allow_nan=False));return int(bool(r['regressions'] or r['structural_changes']))
if __name__=='__main__':raise SystemExit(main())
