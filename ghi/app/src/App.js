import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainPage from './MainPage';
import Nav from './Nav';
import SalespersonForm from './SalespersonForm';
import SalespeopleList from './SalespeopleList';
import CustomerForm from './CustomerForm';
import CustomerList from './CustomerList';
import SaleForm from './SaleForm';
import SalesList from './SalesList';

function App() {
  return (
    <BrowserRouter>
      <Nav />
      <div className="container">
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="salespeople">
            <Route path="/salespeople" element={<SalespeopleList></SalespeopleList>} />
            <Route path="create" element={<SalespersonForm />} />
          </Route>
          <Route path="customers">
            <Route path="/customers" element={<CustomerList></CustomerList>} />
            <Route path="create" element={<CustomerForm />} />
          </Route>
          <Route path="sales">
            <Route path="/sales" element={<SalesList></SalesList>} />
            <Route path="create" element={<SaleForm />} />
          </Route>
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
