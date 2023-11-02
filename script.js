// Get elements for question input and answer output
const questionInput = document.getElementById("question-input");
const answerOutput = document.getElementById("answer-output");

// Function to send the user's question to the server and display the response
async function getGpt3Response(question) {
    try {
        const response = await fetch('http://127.0.0.1:5000/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ question })
        });        

        if (response.ok) {
            const data = await response.json();
            console.log("data :", data)
            answerOutput.innerHTML = data.answer;
        } else {
            answerOutput.innerHTML = 'Error: Unable to fetch response from server';
        }
    } catch (error) {
        answerOutput.innerHTML = 'Error: ' + error;
    }
}

// Event listener for handling user input and generating answers on "Enter" key press
questionInput.addEventListener("keydown", (event) => {
    if (event.key === "Enter") {
        const question = questionInput.value;
        answerOutput.innerHTML = 'Loading...';

        // Call the function to get the response from the server
        getGpt3Response(question);
    }
});
