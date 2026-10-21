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
    pass

# 3. ki nyert ? (dict) -> (város, db)
def find_winner(counts: dict) -> tuple:
    pass

# 4. kiíratás (város, db) -> None
def print_result(winner: tuple) -> None:
    pass

def main():
    votes = read_file('votes.txt')
    normalized_votes = normalize(votes)
    
    print(normalized_votes)


if __name__ == "__main__":
    main()
