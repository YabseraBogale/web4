fetch("http://127.0.0.1:5000/exit_exam_question_answer_api")
    .then((response)=> response.json())
    .then(data=>{
        
    })
    .catch(err=>{
        console.error(err)
    })