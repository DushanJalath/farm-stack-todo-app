
import React from "react";

import TodoItem from "./ToDo";

export default function TodoView(props) {
    return (
        <div>
            <ul>
                {props.list.map(todo => <TodoItem todo={todo} />)}
            </ul>
        </div>
    )
}