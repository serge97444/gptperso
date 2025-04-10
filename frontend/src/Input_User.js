// import {useState} from 'react';
import React, { useEffect, useState } from 'react';
import axios from 'axios'
import {BounceLoader} from "react-spinners";
import ReactMarkdown from "react-markdown";

const api = axios.create({baseURL: 'http://localhost:8080'});

// const Expander = ({title , content})=>{
//     const [isOpen, setIsOpen] = useState(false);
//     return (
//         <div className="expander">
//             <b onClick={()=> setIsOpen(!isOpen)}>{title}</b>
//             {isOpen && <p>{content}</p>}

//         </div>
//     );

// };

function ProvideInput(){
    const [query, setQuery] = useState('');
    const [answer, setAnswer] = useState('');

    const handleSubmit = async(e) =>{
        e.preventDefault();

        console.log(query)
        const response = await api.post('/chat' , {message : query});
        setAnswer(response.data.response);
        console.log(answer)
    }

    return(
    <div className='main-container'>
        <div >Hello from react</div>
        <form className='form' >

            <input className='form-input' type='text' value={query} onChange = {(e) => setQuery(e.target.value) }></input>
            <button className='form-button' type ='submit' onClick={handleSubmit}>Click here to Submit !</button>
        </form>
        <div>
            <h2>Answer : </h2>
            <p>{answer}</p>
        </div>



    </div>
    
    );
}

// function ProvideInput(){
//     const [query, setQuestion] = useState('');
//     const [answer, setAnswer] = useState('');
//     const [isLoading, setIsLoading] = useState(false);
//     // const [documents, setDocuments] = useState([]);

//     const handleSubmit = async(e)=>{ e.preventDefault();
//         console.log(query)
//         const response = await api.post('/chat', {message : query});
//         setAnswer(response.data.response);
//         // setDocuments(response.data.sources)
//         setIsLoading(false);
//     }

//     return(

//         <div className='main-container'>
//         <form className='form'>
//             <input className ="form-input" type="text" value= {query} onChange= {(e)=> setQuestion(e.target.value)} />
//             <button className="form-button" type="submit" onClick={handleSubmit}>Submit</button>
//         </form>
//         {isLoading && (
//             <div className='load-container'>
//                 <BounceLoader color="#3498db"/>
//                 </div>

//         )}
//         <div>
//             <h2>Answer: </h2>
//             <p>{answer}</p>
//         </div>
//         {/* <div>
//             <h2> Documents: </h2>
//             <ul>
//                 {documents.map((documents, index) => (
//                             <Expander key={index} title={documents.page_content.split(" ").slice(0, 5).join(" ") + "..."} content={documents.page_content} source={documents.metadata.source_url}/>
//                             ))}
//             </ul>

//         </div> */}




//         </div>
//     )

// }

export default ProvideInput
