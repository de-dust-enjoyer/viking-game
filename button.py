from types import MethodType
from typing import Optional
import pygame


class Button:
	def __init__(self, id:str, pos:tuple, path_to_img_folder:str, centered:bool = False, method:Optional[MethodType] = None, arg = None):

		self.visible = True
		
		self.images = {"idle": pygame.image.load(f"{path_to_img_folder}{id}_idle.png").convert_alpha()
					, "pressed": pygame.image.load(f"{path_to_img_folder}{id}_pressed.png").convert_alpha()
					, "hover": pygame.image.load(f"{path_to_img_folder}{id}_hover.png").convert_alpha()}
		
		self.image:pygame.Surface = self.images["idle"]

		self.rect:pygame.Rect = self.image.get_rect()
		
		self.clicked = False
		self.was_pressed = False

		self.method:Optional[MethodType] = method
		self.arg = arg


		if centered:
			self.rect.center = pos
		else:
			self.rect.topleft = pos


	def update(self, **kwargs) -> bool: # type:ignore
		if not self.visible:
			return False

		self.image = self.images["idle"]
		if "rel_mouse_pos" in kwargs:
			mouse_pos = kwargs["rel_mouse_pos"]
		else:
			mouse_pos = pygame.mouse.get_pos()

		mouse_pressed = pygame.mouse.get_pressed()[0]

		# check if mouse is over button
		if self.rect.collidepoint(mouse_pos):
			self.image = self.images["hover"]

			if mouse_pressed:
				self.image = self.images["pressed"]
				self.was_pressed = True

			elif self.was_pressed: # mouse was pressed but now realeased over the button
				self.was_pressed = True
				if self.method:
					if self.arg:
						print(self.method, self.arg)
						self.method(self.arg)
					else:
						self.method()
				return True
		else:
			# mouse moved away from button
			self.was_pressed = False

		return False



	def add_method(self, method, arg=None):
		self.method = method
		self.arg = arg