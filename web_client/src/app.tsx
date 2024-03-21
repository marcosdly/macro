import { useState } from "preact/hooks";
import "./app.scss";

export function App() {
  const [count, setCount] = useState(0);

  return (
    <>
      <button
        className="btn btn-primary"
        onClick={() => setCount(count + 1)}
      >{`Click: ${count}`}</button>
    </>
  );
}
