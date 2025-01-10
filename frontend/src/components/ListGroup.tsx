import { useState } from "react";

function ListGroup() {
  let items = ["Item A", "Item B", "Item C", "Item D"];

  const [selectedIndex, setSelectedIndex] = useState(-1);

  return (
    <>
      <h1>List Group</h1>
      {items.length === 0 && <p> No projects found!</p>}
      <ul className="list-group">
        {items.map((item, index) => (
          <li
            className={
              selectedIndex === index
                ? "active list-group-item"
                : "list-group-item"
            }
            key={item}
            onClick={() => {
              setSelectedIndex(index);
            }}
          >
            {item}
          </li>
        ))}
      </ul>
    </>
  );
}

export default ListGroup;
