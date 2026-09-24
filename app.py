"""Audit multiple-choice question structure."""
import argparse,json,re
from pathlib import Path
AMBIGUITY=("always","never","all of the above","none of the above")
def audit_question(q:dict)->dict:
    prompt=str(q.get("prompt","")).strip();options=[str(x).strip() for x in q.get("options",[])];answer=str(q.get("answer","")).strip();issues=[]
    if len(prompt)<10:issues.append("prompt-too-short")
    if len(options)<3:issues.append("too-few-options")
    normalized=[re.sub(r"\s+"," ",x.lower()) for x in options]
    if len(normalized)!=len(set(normalized)):issues.append("duplicate-options")
    if answer not in options:issues.append("answer-not-in-options")
    hits=[word for word in AMBIGUITY if word in prompt.lower() or any(word in x.lower() for x in options)]
    if hits:issues.append("review-absolute-wording")
    return {"id":q.get("id"),"status":"review" if issues else "pass","issues":issues,"matched_wording":hits}
def run(items:list[dict])->dict:return {"question_count":len(items),"results":[audit_question(q) for q in items],"disclaimer":"Structural audit only; educator validates correctness."}
def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("input",nargs="?",default="sample_data.json");print(json.dumps(run(json.loads(Path(p.parse_args().input).read_text())),indent=2))
if __name__=="__main__":main()
