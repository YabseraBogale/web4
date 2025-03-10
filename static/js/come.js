

const vid=document.getElementById("vid")
const recorded=document.getElementById("recorded")
const video=document.getElementById("video")
const start=document.getElementById("start")
const send=document.getElementById("send")
const record=document.getElementById("recorded_video")
const question=document.querySelector(".question")

let mediaRecorder;
let recordchunk=[]
let blob=null
async function startVideoStream(){
    try{    
            
            let stream=await navigator.mediaDevices.getUserMedia({video: true,audio: true})
            video.srcObject=stream
            mediaRecorder=new MediaRecorder(stream)
            mediaRecorder.ondataavailable =(event)=>{
                
                if(event.data.size > 0){
                    recordchunk.push(event.data)
                }
            }
            mediaRecorder.onstop =()=>{
                blob = new Blob(recordchunk,{type:'video/webm'})
                const videourl=URL.createObjectURL(blob)
                record.src=videourl
                video.style.display='none'
                recorded.style.display='block'
                send.disabled=false
                if(stream){
                    stream.getTracks().forEach(track=>{
                        track.stop()
                    })
                }
        }
    }catch(err){
        console.error(err)
    }
    
}
start.addEventListener("click",()=>{
    try{

        recordChunks = []; 
        mediaRecorder.start();
        question.style.display='inline'
        setTimeout(()=>{
            mediaRecorder.stop()
            vid.style.display='none'
            recorded.style.display='inline'
        },3000)        
        
    } catch(err){
        console.error(err);
        
    }

})

send.addEventListener("click",async ()=> {
    if(!blob){
        console.error("No recorded video found")
        return 
    }
    const formData=new FormData()
    formData.append("video",blob,"recorded_video.webm")
    try{
        const response=await fetch("http://127.0.0.1:5000/come",{
            method: "POST",
            body:formData,
        })
        if(response.ok){
            console.log("sent sucessfully");   
        } 
    } catch(err){
        console.error(err);
    }
})

startVideoStream()
