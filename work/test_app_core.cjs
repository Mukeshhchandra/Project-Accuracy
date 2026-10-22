const assert=require('node:assert/strict');
const C=require('../outputs/accuracy/core.js');
const qs=Array.from({length:200},(_,i)=>({id:`Q${i}`,answer:i%4,topic:i<100?'Quant':'GS'}));
const answers={};for(let i=0;i<180;i++)answers[`Q${i}`]=i<150?i%4:(i+1)%4;
const a={id:'test',setId:'mock-01',status:'active',answers,flags:['Q0'],cursor:0,startedAt:1000000000000,endAt:1000010800000};
const r=C.grade(a,qs);assert.deepEqual([r.correct,r.wrong,r.blank,r.attempted,r.score,r.coverage],[150,30,20,180,144,90]);assert.equal(r.accuracy,150/180*100);
assert.equal(C.grade({answers:{}},qs).accuracy,null);assert.equal(C.grade({answers:Object.fromEntries(qs.map(q=>[q.id,(q.answer+1)%4]))},qs).score,-40);
assert.equal(C.remaining(a,a.startedAt),10800);assert.equal(C.remaining(a,a.endAt-1),1);assert.equal(C.remaining(a,a.endAt),0);assert.equal(C.remaining(a,a.endAt+900),0);
assert.equal(C.formatTime(10800),'03:00:00');assert.equal(C.formatTime(0),'00:00:00');
assert.deepEqual(C.select({Q0:0},'Q0',null),{});assert.deepEqual(C.select({},'Q0',0),{Q0:0});assert.deepEqual(C.select({},'Q0',7),{});
const data={version:'test',sets:[{id:'mock-01',questionIds:qs.map(q=>q.id)}],questions:qs};const state={version:1,bankVersion:'test',attempts:[a],bookmarks:['Q0','Q0','invalid'],practice:{Q1:1,invalid:0,Q2:7}};
const restored=C.validateState(state,data);assert.deepEqual(restored.bookmarks,['Q0']);assert.deepEqual(restored.practice,{Q1:1});
for(const mutate of [x=>x.bankVersion='other',x=>x.attempts[0].answers.Q0=4,x=>x.attempts[0].cursor=200,x=>x.attempts[0].endAt++,x=>x.attempts[0].flags=['missing'],x=>x.attempts[0].status='submitted']){const bad=structuredClone(state);mutate(bad);assert.throws(()=>C.validateState(bad,data))}
console.log('PASS: grading, negative marking, blank accuracy, coverage, timer boundaries, answer clearing, backup validation.');
