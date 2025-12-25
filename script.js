async function askEduLift() {
    const level = document.getElementById("level").value;
    const interest = document.getElementById("interest").value;
    const goal = document.getElementById("goal").value;

    const output = document.getElementById("output");
    output.innerText = "✨ EduLift AI is thinking...";

    const response = await fetch("/guidance", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ level, interest, goal })
    });

    const data = await response.json();
    output.innerText = data.reply;
}
