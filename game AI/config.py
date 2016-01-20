# config.py

# configuration for game
game = dict(
    width               = 400,          # game width
    height              = 400,          # game height
    g_name              = "GAME"        # game name
    g_time              = 10000,        # game time
    fps                 = 60,           # frame per second
    n_agents            = 40,           # number of agents
    n_targets           = 20,           # number of targets
    s_agent             = 28,           # size of an agent
    s_target            = 2,            # size of a target
)

image = dict(
    agent               = "agent.png"   # path of agent image file
    target              = "target.png"  # path of target image file
)

# configuration for neural network
nnet = dict(
    n_inputs            = 4,            # number of inputs
    n_outputs           = 2,            # number of outputs
    n_hidden_layers     = 3,            # number of hidden layers
    n_hl_neurons        = 4,            # number of neurons in a hidden layer
    bias                = -1,           # bias
    response            = 1,            # response
)

# configuration for genetic algorithm
ga = dict(
    s_dna               = 10,           # DNA size
    s_pop               = 20,           # population size
    n_gen               = 20,           # number of generations
    p_mut               = 0.1,          # probability of mutation
    p_xover             = 0.1,          # probability of crossover
)
