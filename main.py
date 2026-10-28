def hanoi_solver(total_disk):
    rod_a = list(range(total_disk, 0 ,-1))
    rod_b = []
    rod_c = []

    line = f"{rod_a} {rod_b} {rod_c}"

    moves = []

    moves.append(line)

    def move_disks(count, source, auxiliary, destination):
        if count == 1:
            disk = source.pop()
            destination.append(disk)
            line = f"{rod_a} {rod_b} {rod_c}"
            moves.append(line)
            return
        else:
            move_disks(count - 1, source, destination, auxiliary)
            disk = source.pop()
            destination.append(disk)
            line = f"{rod_a} {rod_b} {rod_c}"
            moves.append(line)

            move_disks(count - 1, auxiliary, source, destination)

    move_disks(total_disk, rod_a, rod_b, rod_c)
    
    return "\n".join(moves)