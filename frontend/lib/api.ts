export async function sendChat(message: string) {
  const response = await fetch("http://localhost:8000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message, project: "ApolloGPT" })
  });
  return response.json();
}

