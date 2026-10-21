# 1. file beolvasása () -> list of string
def read_file(file_name: str) -> list:
    answers = []
    with open(file_name) as f:
        for line in f:
            answers.append(line.strip())
    return answers

# 1.5 normalizálás (list of string) -> list of sting
def normalize(votes: str) -> list:
    return [vote.lower() for vote in votes]

# 2. szavazatok számlálása (list of string) -> dict város: db
def count_votes(votes: list) -> dict:
    counts = {}
    for vote in votes:
        counts[vote] = counts.get(vote, 0) + 1
    return counts

# 3. ki nyert ? (dict) -> dict
def find_winner(counts: dict) -> dict:
    max_votes = max(counts.values())
    cities = []
    
    for city in counts:
        if counts[city] == max_votes:
            cities.append(city)
    
    return {
        'cities':cities,
        'votes': max_votes
    }
    

# 4. kiíratás (város, db) -> None
def print_result(winner: dict) -> None:
    winner_len = len(winner['cities'])
    if(winner_len == 1):
        print(f'Győztes: {winner['city']} ({winner['counts']} szavazat)')
    else:
        print(f'Nincs győztes! Városok {winner['votes']} szavazatot kaptak: {winner['cities']}')
    
def main():
    votes = read_file('votes.txt')
    normalized_votes = normalize(votes)
    counts = count_votes(normalized_votes)
    winner = find_winner(counts)
    print_result(winner)
    

if __name__ == "__main__":
    main()
