import numpy as np
import ga
def main():
    equation_inputs = [15, 3, 2, 5, 9, 20]
    equation_points = [17, 7, 10, 5, 8, 17]   
    num_weights = 6  
    solutions_per_equation_points = 6  
    equation_points_size = (solutions_per_equation_points, num_weights)
    equation_points = np.random.randint(
        low=0, high=2,
        size=equation_points_size)
    
    print("População inicial:")
    print(equation_points)
    nmr_geracao = 5
    num_parents_crossover = 4
    for generation in range(nmr_geracao):
        print(f"\nGeração {generation}")
        fit = ga.fit(equation_inputs, equation_points)
        print("\nfit:")
        print(fit)
        selected_parents = ga.selection(
            equation_points, fit, num_parents_crossover)
        print("\nGenitores escolhidos:")
        print(selected_parents)
        offspring_crossover = ga.crossover(
            selected_parents, (
                solutions_per_equation_points - num_parents_crossover,
                num_weights
            )
        )
        print("\nFilhos gerados por crossover:")
        print(offspring_crossover)
        offspring_mutation = ga.mutation(offspring_crossover)
        print("\nFilhos pós mutação:")
        print(offspring_mutation)
        equation_points[0:selected_parents.shape[0], :] = selected_parents
        equation_points[selected_parents.shape[0]:, :] = offspring_mutation
        print("\nNova população:")
        print(equation_points)
        print("Maior resultado: ", np.max(
            ga.fit(equation_inputs, equation_points)))
    fit = ga.fit(equation_inputs, equation_points)
    best_fit_idx = np.where(fit == np.max(fit))
    print("Maior resultado: ", equation_points[best_fit_idx, :])
    print("fit do maior: ", fit[best_fit_idx])

if __name__ == "__main__":
    main()