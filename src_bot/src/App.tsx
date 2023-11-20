import './App.css'
import {useState} from "react";
import axios, {AxiosResponse} from "axios";


type messageType = { role: string, content: string }

const App = () => {

    const [messages, setMessages] = useState([
        {'role': 'bot', 'content': 'Hi! This is Jarvis, your proprietary data bot. '}
    ]);

    const [userInput, setUserInput] = useState("");

    const handleTextChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setUserInput(event.target.value)
    }

    const sendMessage = (): void => {
        const temp: messageType[] = [];
        messages.forEach((message: messageType) => temp.push(message))
        temp.push({'role': 'user', 'content': userInput});

        axios.post('http://localhost:8080/api/chat', {'query': userInput}).then((response: AxiosResponse<any, any>): void => {
            temp.push({'role': 'bot', 'content': response.data.data});
            setMessages(temp);
            setUserInput("")
        });
    }

    return (
        <>
            <div className="chat-container">
                <div className="chat-header">PK Bot</div>
                <div className="chat-messages" id="chat-messages" >
                    {
                        messages.map((object: messageType, index: number) => {
                            if (object.role === 'bot') {
                                return (
                                    <div className="message bot-message" key={index}>
                                        <div className="message-content">{'Bot: '.concat(object.content)}</div>
                                    </div>

                                )
                            }else{
                                return (
                                    <div className="message user-message" key={index}>
                                        <div className="message-content">{'User: '.concat(object.content)}</div>
                                    </div>

                                )
                            }
                        })
                    }
                </div>
                <div className="user-input-container">
                    <div className="input-box-container">
                        <input type="text" className="input-box" id="user-input"
                               placeholder="Type your message..."
                               onChange={(event: React.ChangeEvent<HTMLInputElement>) => handleTextChange(event)}></input>
                        <div className="chat-icon" onClick={() => sendMessage()}>💬</div>
                    </div>
                </div>
            </div>

            <div className="side-container">
                <div className="upload-button">Upload File</div>
                <input type="file"></input>
            </div>
        </>
    )
}

export default App
