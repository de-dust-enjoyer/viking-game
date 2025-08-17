def get_nearby_tiles(player_pos, chunk_dict, chunk_size, radius_in_chunks_x=1, radius_in_chunks_y=1) -> list:
		chunk_x = int(player_pos[0] // chunk_size)
		chunk_y = int(player_pos[1] // chunk_size)
		nearby_tiles = []
		for dx in range(-radius_in_chunks_x, radius_in_chunks_x +1):
			for dy in range(-radius_in_chunks_y, radius_in_chunks_y +1):
				key = (chunk_x + dx, chunk_y + dy)
				nearby_tiles.extend(chunk_dict.get(key, []))
		return nearby_tiles

def get_nearby_big_tiles(player_pos, chunk_dict, chunk_size, radius_in_chunks_x=1, radius_in_chunks_y=1) -> list:
		chunk_x = int(player_pos[0] // chunk_size)
		chunk_y = int(player_pos[1] // chunk_size)
		nearby_tiles = []
		for dx in range(-radius_in_chunks_x, radius_in_chunks_x +1):
			for dy in range(-radius_in_chunks_y, radius_in_chunks_y +1):
				key = (chunk_x + dx, chunk_y + dy)
				if key in chunk_dict:
					nearby_tiles.append(chunk_dict[key])
		return nearby_tiles