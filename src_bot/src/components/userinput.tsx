import React from "react";

export const UserInput = ({handleTextChange, sendMessage}: any) => {
    return(
        <div className="user-input-container">
            <div className="input-box-container">
                <input type="text" className="input-box" id="user-input"
                       placeholder="Type your message..."
                       onChange={(event: React.ChangeEvent<HTMLInputElement>) => handleTextChange(event)}></input>
                <div className="chat-icon" onClick={() => sendMessage()}>💬</div>
            </div>
        </div>
    )
}