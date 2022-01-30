from simulation.Simulation import Simulation

sim = Simulation()

sim.add_agent('Alice')
sim.add_agent('Bob')

sim.generate_keys('Alice', 'Bob', protocol_name='simple')

