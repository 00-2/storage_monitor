import React, { useEffect } from 'react'
//TODO declare usage of non react-libraries
function App() {
    useEffect(() => {
        fetch("http://localhost:40001/members").then(
            res => res.json()
        ).then(
            data => {
                console.log(data)
            }
        )
    }, [])

    return (
        <div>
        </div>
    )
}

export default App
