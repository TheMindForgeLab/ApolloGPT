import ChatInput from "./ChatInput";
import MessageBubble from "./MessageBubble";

export default function ChatWindow() {
  return (
    <section className="card">
      <div className="section-title">Chat Mode</div>
      <div className="chat-box">
        <MessageBubble speaker="You" text="Create a new content business and build a blog workflow." />
        <MessageBubble speaker="Manager Agent" text="I can create the business scaffold, suggest departments, assign starter agents, and draft the workflow for approval." agent />
      </div>
      <ChatInput />
    </section>
  );
}

