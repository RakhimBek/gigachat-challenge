

<hr>

```javascript

fetch("/api/ask", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
    },
    body: JSON.stringify({
        "name": "string",
        "message": "string",
        "prev": [
            "string"
        ],
        "next": [
            "string"
        ]
    })
})
    .then(x => x.json())
    .then(x => console.log(x))

```