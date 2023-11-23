import {messageType} from "../types/ApplicationTypes.ts";

// @ts-ignore
export const ChatArea = ({messages}: any) => {
    return(
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
    )
}