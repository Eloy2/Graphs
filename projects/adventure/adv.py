from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "C:/Users/Eloy D. Gutierrez/Graphs/projects/adventure/maps/test_line.txt"
# map_file = "C:/Users/Eloy D. Gutierrez/Graphs/projects/adventure/maps/test_cross.txt"
# map_file = "C:/Users/Eloy D. Gutierrez/Graphs/projects/adventure/maps/test_loop.txt"
# map_file = "C:/Users/Eloy D. Gutierrez/Graphs/projects/adventure/maps/test_loop_fork.txt"
map_file = "C:/Users/Eloy D. Gutierrez/Graphs/projects/adventure/maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
def opposite_direction(direction):
    if direction == "n":
        return "s"
    elif direction == "s":
        return "n"
    elif direction == "e":
        return "w"
    elif direction == "w":
        return "e"
traversal_path = []
stack = []
visited = set()
print("START")
while len(visited) < len(world.rooms):
    # rooms we can travel to from current room.
    directions_to_travel = []
    current_room = player.current_room
    # for every exit in current_room
    for direction in current_room.get_exits():
        if current_room.get_room_in_direction(direction) not in visited:
            # if room is not in visited add to rooms we can travel.
            # .get_room_in_direction() returns rooms as ints
            directions_to_travel.append(direction)

    # add current room to visited
    visited.add(current_room)

    if directions_to_travel:
        # randomly choose a direction to travel
        travel_to = random.choice(directions_to_travel)
        # append direction to stack
        stack.append(travel_to)
        # move player to that room
        player.travel(travel_to)
        # add direction to traversal_path
        traversal_path.append(travel_to)
    # else pop from stack and go backwards until we find a room that has directions
    # it can travel to.
    else:
        # pop from stack
        last_direction_moved = stack.pop()
        # go in opposite direction until we find room we can travel to
        direction = opposite_direction(last_direction_moved)
        # move player
        player.travel(direction)
        # append to traversal path
        traversal_path.append(direction)
print("END")
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
