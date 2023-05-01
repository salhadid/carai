import { NavLink } from "react-router-dom";
import { Navbar, Nav } from 'react-bootstrap';
import { Dropdown } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';

function Navigation() {
	return (
		<Navbar bg="success" expand="lg" variant="dark">
			<Navbar.Brand as={NavLink} to="/">
				CarCar
			</Navbar.Brand>
			<Navbar.Toggle aria-controls="navbarSupportedContent" />
			<Navbar.Collapse id="navbarSupportedContent">
				<Nav className="me-auto mb-2 mb-lg-0">
					<Dropdown>
						<Dropdown.Toggle variant="success" id="dropdown-manufacturers">
							Manufacturers
						</Dropdown.Toggle>
						<Dropdown.Menu>
							<Dropdown.Item as={NavLink} to="/manufacturers">
								Manufacturers
							</Dropdown.Item>
							<Dropdown.Item as={NavLink} to="/manufacturers/create">
								Create a Manufacturer
							</Dropdown.Item>
						</Dropdown.Menu>
					</Dropdown>
					<Dropdown>
						<Dropdown.Toggle variant="success" id="dropdown-models">
							Models
						</Dropdown.Toggle>
						<Dropdown.Menu>
							<Dropdown.Item as={NavLink} to="/models">
								Models
							</Dropdown.Item>
							<Dropdown.Item as={NavLink} to="/models/create">
								Create a Model
							</Dropdown.Item>
						</Dropdown.Menu>
					</Dropdown>
					<Dropdown>
						<Dropdown.Toggle variant="success" id="dropdown-automobiles">
							Automobiles
						</Dropdown.Toggle>
						<Dropdown.Menu>
							<Dropdown.Item as={NavLink} to="/automobiles">
								Automobiles
							</Dropdown.Item>
							<Dropdown.Item as={NavLink} to="/automobiles/create">
								Create an Automobile
							</Dropdown.Item>
						</Dropdown.Menu>
					</Dropdown>
					<Dropdown>
						<Dropdown.Toggle variant="success" id="dropdown-salespeople">
							Salespeople
						</Dropdown.Toggle>
						<Dropdown.Menu>
							<Dropdown.Item as={NavLink} to="/salespeople">
								Salespeople
							</Dropdown.Item>
							<Dropdown.Item as={NavLink} to="/salespeople/create">
								Add a Salesperson
							</Dropdown.Item>
						</Dropdown.Menu>
					</Dropdown>
					<Dropdown>
						<Dropdown.Toggle variant="success" id="dropdown-customers">
							Customers
						</Dropdown.Toggle>
						<Dropdown.Menu>
							<Dropdown.Item as={NavLink} to="/customers">
								Customers
							</Dropdown.Item>
							<Dropdown.Item as={NavLink} to="/customers/create">
								Add a Customer
							</Dropdown.Item>
						</Dropdown.Menu>
					</Dropdown>
					<Dropdown>
						<Dropdown.Toggle variant="success" id="dropdown-sales">
							Sales
						</Dropdown.Toggle>
						<Dropdown.Menu>
							<Dropdown.Item as={NavLink} to="/sales">
								Sales
							</Dropdown.Item>
							<Dropdown.Item as={NavLink} to="/sales/create">
								Add a Sale
							</Dropdown.Item>
							<Dropdown.Item as={NavLink} to="/sales/history">
								Salesperson History
							</Dropdown.Item>
						</Dropdown.Menu>
					</Dropdown>
					<Dropdown>
						<Dropdown.Toggle variant="success" id="dropdown-technicians">
							Technicians
						</Dropdown.Toggle>
						<Dropdown.Menu>
							<Dropdown.Item as={NavLink} to="/technicians">
								Technicians
							</Dropdown.Item>
							<Dropdown.Item as={NavLink} to="/technicians/create">
								Add a Technician
							</Dropdown.Item>
						</Dropdown.Menu>
					</Dropdown>
					<Dropdown>
						<Dropdown.Toggle variant="success" id="dropdown-appointments">
							Service Appointments
						</Dropdown.Toggle>
						<Dropdown.Menu>
							<Dropdown.Item as={NavLink} to="/appointments">
								Service Appointments
							</Dropdown.Item>
							<Dropdown.Item as={NavLink} to="/appointments/create">
								Add an Appointment
							</Dropdown.Item>
							<Dropdown.Item as={NavLink} to="/appointments/history">
								Service History
							</Dropdown.Item>
						</Dropdown.Menu>
					</Dropdown>
				</Nav>
			</Navbar.Collapse>
		</Navbar>
	);
}

export default Navigation;
