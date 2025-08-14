from pygame import RESIZABLE
from constants import *
from timer import Timer
from chunking import get_nearby_big_tiles



class CameraGroup(pygame.sprite.Group):
	def __init__(self, surface:pygame.Surface, groups:list, chunk_dict:dict, chunk_size:int, type:str="follow"):
		super().__init__()
		self.type = type
		self.render_dist_x = RENDER_DIST[0] # chunks
		self.render_dist_y = RENDER_DIST[1] # chunks
		self.display_surf = surface
		self.camera_rect = self.display_surf.get_frect()
		self.groups = groups
		self.zoom:float = 1
		self.zoom_target:float = self.zoom # used to lerp()


		self.sprites_drawn = 0

		
		self.zoom_center = pygame.math.Vector2(self.display_surf.get_size()) / 2
		self.offset:pygame.math.Vector2 = pygame.math.Vector2(100,250)

		self.velocity = pygame.Vector2(0, 0)
		self.camera_smoothing = 400
		self.dead_zone = 0.01

		self.target = None
		self.temp_target = None

		self.temp_target_timer = Timer(5)

		self.chunk_dict = chunk_dict
		self.chunk_size = chunk_size
	


	def custom_draw(self):
		w, h = self.display_surf.get_size()
		self.sprites_drawn = 0
		self.zoom_center.update(w / 2, h / 2)
		
		prev_zoom = self.zoom
		if self.zoom != self.zoom_target:
			self.zoom = pygame.math.lerp(self.zoom, self.zoom_target, 0.01)

		if abs(self.zoom - prev_zoom) > 1e-8:
			anchor = self.zoom_center

			self.offset += anchor * (1.0/prev_zoom - 1.0/self.zoom)

		zoom = self.zoom
		if self.type == "follow":
			self.box_movement()
		elif self.type == "mouse":
			pass # future mouse controll camera
		# aduasts the rect to it fits the zoomed screen
		visible_w = w / zoom
		visible_h = h / zoom

		self.camera_rect.topleft = (self.offset.x , self.offset.y)
		self.camera_rect.size = (visible_w, visible_h)

		self.display_surf.fill((91,110,225))
		center_pos = self.camera_rect.center
		nearby_tiles = get_nearby_big_tiles(center_pos, self.chunk_dict, self.chunk_size, self.render_dist_x, self.render_dist_y)

		for sprite in nearby_tiles:
			sprite_pos = sprite.rect.topleft
			adjusted_pos_x = (sprite_pos[0] - self.offset.x) * zoom
			adjusted_pos_y = (sprite_pos[1] - self.offset.y) * zoom
			self.display_surf.blit(sprite.scale_by(zoom), (int(adjusted_pos_x), int(adjusted_pos_y)))
			self.sprites_drawn += 1




		for group in self.groups:
			for sprite in group:
				if not sprite.dead:
					sprite_pos = pygame.Vector2(sprite.rect.topleft)
					adjusted_pos = ((sprite_pos - self.offset) * zoom)
					self.display_surf.blit(sprite.scale_by(zoom), adjusted_pos)
					self.sprites_drawn += 1


	def box_movement(self):
		if self.temp_target_timer.update():
			self.temp_target = None
		self.velocity = pygame.Vector2(0, 0)
		if self.temp_target:
			self.velocity = (pygame.Vector2(self.temp_target.collision_rect.center) - pygame.Vector2(self.camera_rect.center)) / self.camera_smoothing
			if abs(self.velocity.length()) < self.dead_zone:
				self.velocity = pygame.Vector2(0,0)

		elif self.target:
			self.velocity = (pygame.Vector2(self.target.collision_rect.center) - pygame.Vector2(self.camera_rect.center)) / self.camera_smoothing
			if abs(self.velocity.length()) < self.dead_zone:
				self.velocity = pygame.Vector2(0,0)

		self.offset += self.velocity




	def set_target(self, target, permanent=False, duration=None):
		if permanent:
			self.target = target
		else:
			self.temp_target = target
			if duration:
				self.temp_target_timer.set_duration(duration)
				self.temp_target_timer.start()

	def set_position(self, position:tuple):
		self.offset.update(position[0] -self.camera_rect.width / 2, position[1] -self.camera_rect.height / 2)

	def set_zoom(self, new_zoom:float):
		self.zoom_target = new_zoom
