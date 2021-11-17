# File name: accident.py

from abc import ABC, abstractmethod
from kivy.core.audio import SoundLoader
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from random import choice
from kivy.animation import Animation
from kivy.clock import Clock

class Accident(ABC):
    intro = 'BREAKING NEWS: '

    def __init__(self, name, 
                 headlines, 
                 sound, 
                 position = 0, 
                 slug = None, 
                 image = None,
                 game=None):
        self.name = name
        self.headlines = headlines
        self.sound = SoundLoader.load(sound)
        self.position = position
        self.slug = slug
        self.image = image
        self.game = game

    @abstractmethod
    def happen(self, autoplay=True, loop=False):
        if loop:
            self.sound.loop = True

        if autoplay:
            self.sound.play()

        headline = choice(self.headlines)
        label = Label(markup = True,
                      text = f'[b][color=ff3333]{self.slug.name} {headline}[/color][/b]', 
                      text_size = (400, 100),
                      halign = 'left',
                      valign = 'center')

        popup_image = Image(source = self.slug.front_image, size_hint = (.2, 1)) 

        content = BoxLayout()      
        content.add_widget(popup_image)
        content.add_widget(label)

        popup = Popup(title = self.intro,
                      title_color = [.9, .2, 0, 1],  # red
                      content = content,
                      size_hint = (None, None),
                      size = (600, 150),
                      pos_hint = {'center_x': .5, 'top': 1},
                      background_color = [0, 0, 0, .2])
        
        popup.open()

    @abstractmethod
    def reset(self):
        pass

### BROKEN LEG ###
class BrokenLegAccident(Accident):
    name = 'Broken Leg'

    headlines = [
        "just broke his leg and is grounded!", 
        "broke his leg, which is practically all he consists of!", 
        "suffered from an open fracture. All he can do now is watch the others win!", 
        "broke his only leg and now looks pretty helpless!", 
        "tripped over a root and broke his leg!"]

    sound = 'assets/sounds/Accidents/Broken Leg.mp3'

    def __init__(self, **kwargs):
        super().__init__(name=self.name, headlines=self.headlines, 
                         sound=self.sound, **kwargs)

    def happen(self):
        super().happen()
        self.slug.run_animation.stop(self.slug)
        self.slug.normal_image = self.slug.body.source 
        self.slug.body.source = ('atlas://assets/accidents/accidents/broken leg ' 
                                 + self.slug.name.lower())                                 
        self.slug.body.x += 10

    def reset(self):
        self.slug.body.source = self.slug.normal_image
        self.slug.body.x -= 10

### OVERHEAT ###
class OverheatAccident(Accident):
    name = 'Overheat'

    headlines = [
        "has been running faster than he should have. He burned of overheat!", 
        "burned by friction. Needs to cool down a bit before the next race!", 
        "roasted on the track from overheat. He's been running way too fast!", 
        "looks like he has been running faster than his body cooling system can handle!", 
        "shouldn't have been speeding like that. Overheating can be dangerous!"]

    sound = 'assets/sounds/Accidents/Overheat.mp3'

    def __init__(self, **kwargs):
        super().__init__(name=self.name, headlines=self.headlines, 
                         sound=self.sound, **kwargs)

    def happen(self):
        super().happen()   
        self.slug.run_animation.stop(self.slug) 
        self.slug.eye_animation.cancel(self.slug)
        self.slug.normal_body_image = self.slug.body.source 
        self.slug.normal_eye_image = self.slug.left_eye.source
        self.slug.body.source = 'atlas://assets/accidents/accidents/overheat body'
        self.slug.left_eye.source = 'atlas://assets/accidents/accidents/overheat eye'
        self.slug.right_eye.source = 'atlas://assets/accidents/accidents/overheat eye' 

    def reset(self):
        self.slug.body.source = self.slug.normal_body_image
        self.slug.left_eye.source = self.slug.normal_eye_image
        self.slug.right_eye.source = self.slug.normal_eye_image
        self.slug.eye_animation.start(self.slug)

### HEART ATTACK ###
class HeartAttackAccident(Accident):
    name = 'Heart Attack'

    headlines = [
        "had a heart attack. Definitely needs a rest!",
        "has a poor heart condition. Hadn't he stopped now, it could have killed him!",
        "beaten by cardiac infarction. He'd better go to hospital asap!",
        "almost killed by heart attack. He had a really narrow escape!",
        "beaten by his weak heart. He'd better get some rest!"]

    sound = 'assets/sounds/Accidents/Heart Attack.mp3'
    image = 'atlas://assets/accidents/accidents/heart attack'

    def __init__(self, **kwargs):
        super().__init__(name=self.name, headlines=self.headlines, 
                         sound=self.sound, image=self.image, **kwargs)

    def happen(self):
        super().happen(loop=True)
        self.slug.run_animation.stop(self.slug) 
        self.heart = Image(source = self.image)
        self.heart.size_hint = .8, .8
        self.heart.x = self.slug.body.x + 40
        self.heart.y = self.slug.body.y + 3
        self.slug.add_widget(self.heart)
        self.heart_animation = (Animation(size_hint = (.6, .6), 
                                duration = .2, t = 'out_back') 
                               + Animation(size_hint = (.8, .8), 
                                duration = .62, t = 'out_back'))
        self.heart_animation.repeat = True
        self.heart_animation.start(self.heart)

    def reset(self):
        self.sound.stop()
        self.heart_animation.cancel(self.heart)
        self.slug.remove_widget(self.heart)

### GRASS ###
class GrassAccident(Accident):
    name = 'Grass'

    headlines = [
        "just found magic grass. It's famous for powering slugs up!", 
        "just about to speed up after eating magic grass!", 
        "powered up by magic grass found unexpectedly on the track!", 
        "seems to be full of beans after having eaten the magic grass on his way!", 
        "heading perhaps even for victory after his magic grass meal!"]

    sound = 'assets/sounds/Accidents/Grass.mp3'
    image = 'atlas://assets/accidents/accidents/grass'

    def __init__(self, **kwargs):
        super().__init__(name=self.name, headlines=self.headlines, 
                         sound=self.sound, image=self.image, **kwargs)

    def happen(self):
        super().happen()
        self.slug.run_animation.stop(self.slug)
        self.grass = Image(source = self.image)
        self.grass.x = self.slug.body.x + 90
        self.slug.add_widget(self.grass, index=-1)
        Clock.schedule_once(self.continue_race, 2)

    def continue_race(self, dt):
        self.slug.remove_widget(self.grass)
        self.sound.stop()
        self.slug.run(acceleration=10).start(self.slug)
        self.slug.run_animation.bind(on_progress=self.game.while_running)
        self.slug.run_animation.bind(on_complete=self.game.finish_race)

    def reset(self):
        pass

### ASLEEP ###
class AsleepAccident(Accident):
    name = 'Asleep'

    headlines = [
        "just fell asleep for a while after the long and wearisome running!", 
        "having a nap. He again has chosen just the perfect time for that!", 
        "sleeping instead of running. It's getting one of his bad habits!", 
        "always takes a short nap at this time of the day, no matter what he's doing!", 
        "knows how important sleep is. Even if it's not the best time for that!"]

    sound = 'assets/sounds/Accidents/Asleep.mp3'

    def __init__(self, **kwargs):
        super().__init__(name=self.name, headlines=self.headlines, 
                         sound=self.sound, **kwargs)

    def happen(self):
        super().happen(loop=True)
        self.slug.run_animation.stop(self.slug)  
        self.slug.eye_animation.cancel(self.slug)
        self.asleep_animation = (Animation(size_hint = (1.05, 1.05), duration = 2.6) 
                                + Animation(size_hint = (1, 1), duration = 3))        
        self.asleep_animation.repeat = True
        self.asleep_animation.start(self.slug.body)

    def reset(self):
        self.sound.stop()
        self.asleep_animation.cancel(self.slug.body)
        self.slug.eye_animation.start(self.slug)

### BLIND ###
class BlindAccident(Accident):
    name = 'Blind'

    headlines = [
        "gone blind. Now staggering to find his way!", 
        "shouldn't have been reading in dark. Now it's hard to find the way!",
        "temporarily lost his eyesight. Now it's difficult for him to follow the track!", 
        "trying hard to find his way after going blind on track!", 
        "staggering to finish the race after going blind because of an infection!"]

    sound = 'assets/sounds/Accidents/Blind.mp3'

    def __init__(self, **kwargs):
        super().__init__(name=self.name, headlines=self.headlines, 
                         sound=self.sound, **kwargs)

    def happen(self):
        super().happen()
        self.slug.run_animation.stop(self.slug) 
        self.slug.run(acceleration=.7).start(self.slug)
        self.slug.run_animation.bind(on_progress=self.game.while_running)
        self.slug.run_animation.bind(on_complete=self.game.finish_race)
        self.slug.eye_animation.cancel(self.slug)   
        self.slug.left_eye.opacity = 0
        self.slug.right_eye.opacity = 0  
        self.slug_y = self.slug.body.y
        self.stagger_animation = (Animation(y = self.slug.body.y + 10, duration = 1) 
                               + Animation(y = self.slug.body.y - 10, duration = 1))              
                
        self.stagger_animation.repeat = True
        self.stagger_animation.start(self.slug.body)

    def reset(self):
        self.slug.left_eye.opacity = 1
        self.slug.right_eye.opacity = 1
        self.stagger_animation.cancel(self.slug.body)
        self.slug.body.y = self.slug_y

### PUDDLE ###
class PuddleAccident(Accident):
    name = 'Puddle'

    headlines = [
        "drowning in a puddle of water!", 
        "beaten by yesterday's heavy rainfalls. Just drowning in a puddle!", 
        "shouldn't have skipped his swimming lessons. Drowning in a puddle now!", 
        "has always neglected his swimming lessons. How wrong he's been!", 
        "disappearing in a puddle of water formed afted heavy rainfall!"]

    sound = 'assets/sounds/Accidents/Drown.mp3'
    image = 'atlas://assets/accidents/accidents/puddle'

    def __init__(self, **kwargs):
        super().__init__(name=self.name, headlines=self.headlines, 
                         sound=self.sound, image=self.image, **kwargs)

    def happen(self, autoplay=False):
        super().happen()
        self.puddle = Image(source = self.image)
        self.puddle.pos = 220, 75 - self.game.slugs.index(self.slug) * 50
        self.track = self.game.track
        self.track.add_widget(self.puddle, index=-1)
        self.slug.run_animation.bind(on_progress=self.drown)

    def drown(self, animation, slug, progression):
        if slug.x >= 600:
            animation.stop(slug)
            self.drowning_animation = (Animation(x = 680, duration = 2, t ='out_quad') 
                                   + Animation(opacity = 0, duration = 3))            
            self.drowning_animation.start(slug) 
            self.sound.play()         

    def reset(self):
        self.drowning_animation.stop(self.slug)
        if self.sound.state == 'play':
            self.sound.stop()
        self.slug.opacity = 1
        self.track.remove_widget(self.puddle)

### ELECTROSHOCK ###
class ElectroshockAccident(Accident):
    name = 'Electroshock'

    headlines = [
        "speeding up after being struck by lightning!", 
        "powered up by lightning. Now running really fast!", 
        "hit by electric discharge. Seems to have been powered up by it!", 
        "accelerated by a series of electric discharges!", 
        "now running much faster after being struck by lightning!"]

    sound = 'assets/sounds/Accidents/Electroshock.mp3'
    image = 'atlas://assets/accidents/accidents/electroshock'

    def __init__(self, **kwargs):
        super().__init__(name=self.name, headlines=self.headlines, 
                         sound=self.sound, image=self.image, **kwargs)

    def happen(self):
        super().happen(loop=True)
        self.bolt = Image(source = self.image)
        self.bolt.x = self.slug.body.x
        self.slug.add_widget(self.bolt)

        self.slug.run_animation.cancel(self.slug)
        self.slug.run(acceleration=5).start(self.slug)
        self.slug.run_animation.bind(on_progress=self.game.while_running)
        self.slug.run_animation.bind(on_complete=self.game.finish_race)

        self.bolt_animation = (Animation(opacity = 0, duration = .2) 
                               + Animation(opacity = 1, duration = .1)
                               + Animation(opacity = .2, duration = .05)
                               + Animation(opacity = 1, duration = .05))
           
        self.bolt_animation.repeat = True
        self.bolt_animation.start(self.bolt)

    def reset(self):
        self.bolt_animation.cancel(self.bolt)
        self.slug.remove_widget(self.bolt)
        self.sound.stop()

### TURNING BACK ###
class TurningBackAccident(Accident):
    name = 'Turning Back'

    headlines = [
        "has forgotten to turn off the gas. Must hurry home before it's too late!",
        "just received a phone call. His house is on fire. No time to lose!", 
        "seems to have more interesting stuff to do than racing.", 
        "seems to have lost orientation. Well, how these little brains work!", 
        "has left his snack in the kitchen. He won't race when he's hungry!"]

    sound = 'assets/sounds/Accidents/Turning Back.mp3'

    def __init__(self, **kwargs):
        super().__init__(name=self.name, headlines=self.headlines, 
                         sound=self.sound, **kwargs)

    def happen(self):
        super().happen()

        # Stop the running animation.
        self.slug.run_animation.stop(self.slug) 

        # Create the turn animation and start it on the slug.     
        self.turn_animation = Animation(x_scale = -1, duration = 2)
        self.turn_animation.start(self.slug)

        # Bind the continue_race method to the on_complete event
        # of the turn animation.
        self.turn_animation.bind(on_complete=self.continue_race)

    # The slug should continue the race in the opposite direction.
    def continue_race(self, animation, slug):
        self.slug.run(backward=True).start(self.slug)

        # The slug must be able to finish the race.
        self.slug.run_animation.bind(on_complete=self.game.finish_race)

    def reset(self):
        self.slug.x_scale = 1

### SHOOTING EYES ###
class ShootingEyesAccident(Accident):
    name = 'Shooting Eyes'

    headlines = [
        "shooting his eyes. Is he ever going to stop cheating?", 
        "just shot his eyes. It seems he would do anything to win!", 
        "sacrificing his eyes for victory's sake!", 
        "shooting his eyes for victory and hoping for quick regeneration!", 
        "too slow to win? Maybe him, but who knows, possibly not his eyes!"]

    sound = 'assets/sounds/Accidents/Shooting Eyes.mp3'

    def __init__(self, **kwargs):
        super().__init__(name=self.name, headlines=self.headlines, 
                         sound=self.sound, **kwargs)

    def happen(self):
        super().happen()

    def reset(self):
        pass

### RUBBERIZED ###
class RubberizedAccident(Accident):
    name = 'Rubberized'

    headlines = [
        "stretching like rubber. This can help!", 
        "stretching for victory. Seems to be approaching finish line faster!", 
        "has never forgotten he was an eraser as a kid.", 
        "cheating again. This time pretending to be a piece of rubber!", 
        "just discovered his ability to stretch like rubber. Why not use it right now?"]

    sound = 'assets/sounds/Accidents/Rubberizer.mp3'

    def __init__(self, **kwargs):
        super().__init__(name=self.name, headlines=self.headlines, 
                         sound=self.sound, **kwargs)

    def happen(self):
        super().happen()

    def reset(self):
        pass

### DEVOURED ###
class DevouredAccident(Accident):
    name = 'Devoured'

    headlines = [
        "devoured by the infamous slug monster. Bad luck!", 
        "just swallowed by the terrible slug monster!", 
        "next on the long list of the slug monster's victims!", 
        "has never suspected he's gonna end up as a snack!", 
        "devoured by the legendary slug monster from the nearby swamps!"]

    sound = 'assets/sounds/Accidents/Devoured.mp3'
    image = 'atlas://assets/accidents/accidents/slug monster'

    def __init__(self, **kwargs):
        super().__init__(name=self.name, headlines=self.headlines, 
                         sound=self.sound, image=self.image, **kwargs)

    def happen(self):
        super().happen()

    def reset(self):
        pass
