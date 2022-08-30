import numpy as np
from scipy.linalg import eig

GO = 0; A1 = 1; CC1 = 2; A2 = 3; T1 = 4; R1 = 5; B1 = 6; CH1 = 7; B2 = 8; B3 = 9
JAIL = 10; C1 = 11; U1 = 12; C2 = 13; C3 = 14; R2 = 15; D1 = 16; CC2 = 17
D2 = 18; D3 = 19; FP = 20; E1 = 21; CH2 = 22; E2 = 23; E3 = 24; R3 = 25; F1 = 26
F2 = 27; U2 = 28; F3 = 29; G2J = 30; G1 = 31; G2 = 32; CC3 = 33; G3 = 34
R4 = 35; CH3 = 36; H1 = 37; T2 = 38; H2 = 39
labels = ['GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3', 'JAIL',
          'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3', 'FP', 'E1',
          'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3', 'G2J', 'G1', 'G2',
          'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2']

def cross_sum(S):
  return [(a + b) for a in S for b in S]

def two_dice_distribution(num_sides):  
  outcomes = cross_sum(range(1, num_sides+1))
  D = np.array([0] * 40)
  for outcome in outcomes:
    D[outcome] += 1
  D = 1 / (num_sides * num_sides) * D
  return D

def apply_chance_card(x):
  for CC in [CC1, CC2, CC3]:
    p_cc = x[CC]
    x[CC] *= 14 / 16
    x[GO] += 1 / 16 * p_cc
    x[JAIL] += 1 / 16 * p_cc

nearest_railway = {CH1: R2, CH2: R3, CH3: R1}
nearest_utility = {CH1: U1, CH2: U2, CH3: U1}

def apply_community_chest_card(x):
  for CH in [CH1, CH2, CH3]:
    p_ch = x[CH]
    x[CH] *= 6/16
    cards = [GO, JAIL, C1, E3, H2, R1, CH-3, 
             nearest_railway[CH], 
             nearest_railway[CH], 
             nearest_utility[CH]]
    for card in cards:
      x[card] += 1/16 * p_ch

def apply_go_to_jail(x):
  x[JAIL] += x[G2J]
  x[G2J] = 0

def dice_distribution(cell_index, num_sides):
  distribution = two_dice_distribution(num_sides)
  distribution = np.roll(distribution, cell_index)
  apply_chance_card(distribution)
  apply_community_chest_card(distribution)
  apply_go_to_jail(distribution)
  return distribution

def monopoly_transition_matrix(num_sides):
  rows = []
  for i in range(40):
    distribution = dice_distribution(i, num_sides)
    rows.append(distribution)
  return np.matrix(rows)

M = monopoly_transition_matrix(4)
eigenvalues, eigenvectors = eig(M.T)
steady_state = eigenvectors.T[0].real
steady_state /= sum(steady_state)
cells = [(p, i) for i, p in enumerate(steady_state)]
"".join([str(c).rjust(2, '0') for _, c in sorted(cells, reverse=True)[:3]])