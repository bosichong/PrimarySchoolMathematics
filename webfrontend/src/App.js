
import './App.css';
import routes from './routes/index.js'
import { useRoutes } from "react-router-dom";



function App() {
  const element = useRoutes(routes)
  return (
    <div>
      {element}
    </div>
    
  );
}

export default App;
