export default function MessageBubble({ speaker, text, agent = false }: { speaker: string; text: string; agent?: boolean }) {
  return (
    <div className={`message ${agent ? "agent" : ""}`}>
      <strong>{speaker}</strong>
      <div>{text}</div>
    </div>
  );
}

