from graph import Graph

g = Graph()

g.add_edge("Alandroal", "Redondo", 25)
g.add_edge("Redondo", "Monsaraz", 30)
g.add_edge("Monsaraz", "Barreiro", 120)
g.add_edge("Barreiro", "Baixa da Banheira", 5)
g.add_edge("Baixa da Banheira", "Moita", 7)
g.add_edge("Moita", "Alcochete", 20)
g.add_edge("Alcochete", "Lisboa", 20)
g.add_edge("Vendas Novas", "Lisboa", 50)
g.add_edge("Montemor", "Vendas Novas", 15)
g.add_edge("Evora", "Montemor", 20)
g.add_edge("Estremoz", "Evora", 40)
g.add_edge("Borba", "Estremoz", 15)
g.add_edge("Elvas", "Borba", 15)
g.add_edge("Elvas", "Arrailos", 50)
g.add_edge("Arrailos", "Alcácer", 90)
g.add_edge("Alcácer", "Palmela", 35)
g.add_edge("Palmela", "Almada", 25)
g.add_edge("Palmela", "Barreiro", 25)
g.add_edge("Almada", "Lisboa", 15)
g.add_edge("Alandroal", "Elvas", 15)

g.set_h("Elvas", 270)
g.set_h("Alandroal", 180)
g.set_h("Arrailos", 220)
g.set_h("Borba", 250)
g.set_h("Redondo", 170)
g.set_h("Monsaraz", 120)
g.set_h("Barreiro", 30)
g.set_h("Baixa da Banheira", 33)
g.set_h("Moita", 35)
g.set_h("Alcochete", 26)
g.set_h("Lisboa", 0)
g.set_h("Alcácer", 140)
g.set_h("Palmela", 85)
g.set_h("Almada", 25)
g.set_h("Estremoz", 145)
g.set_h("Evora", 95)
g.set_h("Montemor", 70)
g.set_h("Vendas Novas", 45)

print(g.m_graph)
print(g.a_star("Elvas", "Lisboa"))
