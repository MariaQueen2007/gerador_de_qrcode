import { 
    createRoutesFromElements,
    createBrowserRouter,
    Route,
} from "react-router-dom";
import Home from "../pages/home";
import Contact from "../pages/contato";
import Root from "../pages/root";
import EditarContato from "../pages/editar-contato";
  
const routes = [
    {
        path: "/",
        element: <Root />
    },
    {
        path: "contato/:contatoId/editar",
        element: <EditarContato />
    },
    {
      path: "contato/:contatoId",
      element: <Contact />
    },
    {
      path: "home",
      element: <Home />
    }
]
  
const router = createBrowserRouter(
    createRoutesFromElements(
      (routes.map((route, index) => {
        return <Route path={route.path} element={route.element} />
      }))
    )
);
export default router;


/*a linha 1 faz a importação das coisas que vão ser usadas no código
/* nas linhas 2, 3 e 4 ele importa as coisas
/* nas linhas 6, 7, 8 e 9 ele importa a home, o contato a root e o editar contato e as páginas chamando as páginas a serem usadas




