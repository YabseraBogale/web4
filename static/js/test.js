fetch("http://127.0.0.1:5000/exit_exam_question_answer_api")
    .then((response)=> response.json())
    .then(data=>{
        const question=document.getElementById("question")
        question.innerText=data[0][0]
        let choice_a = document.getElementById("a")
        let choice_b = document.getElementById("b")
        let choice_c = document.getElementById("c")
        let choice_d = document.getElementById("d")
        let anwser = document.querySelector("anwser")
        let explanation=document.querySelector("explanation")
        choice_a.innerText=data[0][1]
        choice_b.innerText=data[0][2]
        choice_c.innerText=data[0][3]
        choice_d.innerText=data[0][4]
        
    })
    .catch(err=>{
        console.error(err)
    })