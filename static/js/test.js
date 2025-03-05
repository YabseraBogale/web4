let number=0
fetch("http://127.0.0.1:5000/exit_exam_question_answer_api")
    .then((response)=> response.json())
    .then(data=>{
        const question=document.getElementById("question")
        question.innerText=data[number][0]
        let choice_a = document.getElementById("a")
        let choice_b = document.getElementById("b")
        let choice_c = document.getElementById("c")
        let choice_d = document.getElementById("d")
        let anwser = document.getElementById("answer")
        let explanation=document.getElementById("explanation")
        choice_a.innerText=data[number][1]
        choice_b.innerText=data[number][2]
        choice_c.innerText=data[number][3]
        choice_d.innerText=data[number][4]
        anwser.innerText="Answer: "+data[number][5]
        explanation.innerText="Explanation: "+data[number][6]
        
    })
    .catch(err=>{
        console.error(err)
    })