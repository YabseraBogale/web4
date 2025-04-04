let number=0
// to be changed to the domain name
fetch("http://127.0.0.1:5000/exit_exam_question_answer_api")
    .then((response)=> {
        
        return response.json()
    } )
    .then(data=>{
        
        const question=document.getElementById("question")
        let reload=document.getElementById("reload")
        let choice_a = document.getElementById("a")
        let choice_b = document.getElementById("b")
        let choice_c = document.getElementById("c")
        let choice_d = document.getElementById("d")
        let anwser = document.getElementById("answer")
        let explanation=document.getElementById("explanation")
        let previous=document.getElementById("previous")
        let next=document.getElementById("next")
        let check_answer=document.getElementById("check_answer")
        let radio=document.getElementsByName("choice")
        let goto=document.querySelectorAll(".goto")

        reload.addEventListener("click",function(){
            window.location.reload()
        })

        goto.forEach(item=>{
           
            item.addEventListener("click",function(){
                let number_in=parseInt(item.innerText)-1
                number=number_in
                question.innerText=data[number_in][0]
                choice_a.innerText=data[number_in][1]
                choice_b.innerText=data[number_in][2]
                choice_c.innerText=data[number_in][3]
                choice_d.innerText=data[number_in][4]
                anwser.innerText="Answer: "+data[number_in][5]
                explanation.innerText="Explanation: "+data[number_in][6]
                detail.style.visibility='hidden'
                radio[0].checked=false
                radio[1].checked=false
                radio[2].checked=false
                radio[3].checked=false
                
            })
            
        })
        
        question.innerText=data[number][0]
        choice_a.innerText=data[number][1]
        choice_b.innerText=data[number][2]
        choice_c.innerText=data[number][3]
        choice_d.innerText=data[number][4]
        anwser.innerText="Answer: "+data[number][5]
        explanation.innerText="Explanation: "+data[number][6]
        
        
        next.addEventListener("click",function(){
            if(number<99){
                number+=1
                question.innerText=data[number][0]
                choice_a.innerText=data[number][1]
                choice_b.innerText=data[number][2]
                choice_c.innerText=data[number][3]
                choice_d.innerText=data[number][4]
                anwser.innerText="Answer: "+data[number][5]
                explanation.innerText="Explanation: "+data[number][6]
                detail.style.visibility='hidden'
                radio[0].checked=false
                radio[1].checked=false
                radio[2].checked=false
                radio[3].checked=false
                
            }
            
        })
        previous.addEventListener("click",function(){
            if(number>0){
                number-=1
                question.innerText=data[number][0]
                choice_a.innerText=data[number][1]
                choice_b.innerText=data[number][2]
                choice_c.innerText=data[number][3]
                choice_d.innerText=data[number][4]
                anwser.innerText="Answer: "+data[number][5]
                explanation.innerText="Explanation: "+data[number][6]
                detail.style.visibility='hidden'
                radio[0].checked=false
                radio[1].checked=false
                radio[2].checked=false
                radio[3].checked=false
            } 
            
        })

       
        check_answer.addEventListener("click",function(){
            detail.style.visibility='visible'
            goto[number].style.backgroundColor="hsl(210deg 10% 90%)"
            goto[number].style.color="hsl(210deg 40% 16%)"

        })
        }
        
    )
    .catch(err=>{
        console.error(err)
    })

