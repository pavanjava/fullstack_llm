import './App.css'
import React, {useState} from "react";
import axios, {AxiosResponse} from "axios";
import loader from './assets/loader.gif'
import {messageType} from "./types/ApplicationTypes.ts";
import {ChatArea} from "./components/chatarea.tsx";
import {UserInput} from "./components/userinput.tsx";
import {FileUploader} from "./components/knowledge-expoter.tsx";

const App = () => {

    const [messages, setMessages] = useState([
        {'role': 'bot', 'content': 'Hi! This is Jarvis, your proprietary data bot. '}
    ]);

    const [userInput, setUserInput] = useState("");

    const handleTextChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setUserInput(event.target.value)
    }

    const [showLoader, setShowLoader] = useState(false)

    const sendMessage = (): void => {
        const temp: messageType[] = [];
        messages.forEach((message: messageType) => temp.push(message))
        temp.push({'role': 'user', 'content': userInput});
        setShowLoader(true)
        axios.post('http://localhost:8080/api/chat', {'query': userInput}).then((response: AxiosResponse<any, any>): void => {
            if(userInput.includes("database:")){
                temp.push({'role': 'bot', 'content': 'Result= '.concat(response.data.data.result).concat("\n Query= ").concat(response.data.data.query)});
            }else{
                temp.push({'role': 'bot', 'content': response.data.data});
            }
            setShowLoader(false);
            setMessages(temp);
            setUserInput("")
        });
    }

    return (
        <>
            <div className="chat-container">
                <div className="chat-header">PK Bot</div>
                <ChatArea messages={messages}/>
                <div>
                    {
                        showLoader?<img src={loader} className={'loader'}/>:''
                    }
                </div>
                <UserInput handleTextChange={handleTextChange} sendMessage={sendMessage}/>
            </div>
            <FileUploader/>
        </>
    )
}

export default App
