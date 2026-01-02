
import numpy as np
def receive_round_setting():
    round_settings = input()
    N, K, Q = round_settings.split(' ')
    N, K, Q = int(N), int(K), int(Q)
    participants = np.full(N, K, dtype='i')
    round_settings = {'N':N, 'K':K, 'Q':Q,
                    'participants':participants}
    return round_settings

def answer_question(round_settings):
    round_settings['participants'] -= 1*round_settings['Q']
    answerers = np.zeros(shape=round_settings['N'], dtype='i')
    for _ in range(round_settings['Q']):
        answerer = int(input()) - 1
        answerers[answerer] += 1
    round_settings['participants'] += answerers
    return round_settings
        
def announce_resutl(round_setting):

    [print('Yes') if participant > 0 else print('No')
    for participant in round_settings['participants']]

if __name__ == '__main__':
    round_settings = receive_round_setting()
    if round_settings['Q'] < round_settings['K']:
        announce_resutl(round_settings)
    else:
        round_settings = answer_question(round_settings)
        announce_resutl(round_settings)
    # round_settings = receive_round_setting()
    # round_settings = answer_question(round_settings)
    # announce_resutl(round_settings)
