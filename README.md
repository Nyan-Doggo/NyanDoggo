# Welcome to NyanDoggo.com!

## SomeRPG and the problems with cameras!
### (28. nov 2020)
so i've been working on SomeRPG for a while now, it is a 3rd person Adventure RPG about
collecting cool items, however, there is a slight problem, see i made a [video](https://youtu.be/zriUTg_Tk8U) about
the cameras i used in the game, however, they dont necesarily work as well as i had hoped, so i've been spending
some time reworking the system. i am considering writing a post on what is going wrong here, im just kinda stuck
it seems, but i'll figure it out during the week, you can expect a new video next week about this!

### (30. nov 2020)
those cameras? i havent done a video yet, but im considering it, strongly, maybe under the title
"Video Game Cameras, REEEEEEEEEE!!!", or maybe i'll choose something else. so my problem was two-fold.
let me first state: i am not a master at this, there might be a solution far simpler that i've come to ignore.
now then; imagine a point, this could be a car, a player character, your house... i guess not your house. preferably
something that moves about at a speed greater then 1 m/s along a surface, (walking and driving are good, jumping isnt as usefull)
what we want here, is simply to have two cameras, one of them is a orbital camera, and the other is a following camera,
if you can guess how they work i'll give you 2 points!

**the orbital camera:**
this is a simple device, partly, it is a camera. that takes in 2 angles, and a radius, it also takes in a base offset,
the process, is that we take our base offset and rotate it, along the cameras right hand side, or the x-axis in local space,
this gives us a vertical elevation, once we've used this method to adjust the hight of our camera, we then rotate our camera along the
local z-axis of the player, also known as "up", this gives us a rotation to the left or right of the player, finnaly we add our
radius to the cameras position, which is done thru normalizing the adjusted offset, so that the angle to the player remains the same,
but the distance becomes one, and then multiplying this with the radius we want.

**the following camera:**
this is also a relatively simple device, it follows the same principles as the orbital camera, but it does not take in
any input that dictates a horizontal rotation, that means the camera can adjust up and down, but can not rotate around the "up" axis,
so it will always remain behind the player.

**character rotation:**
our character can acutally turn around, (this is why we should imagine a character over a house), and (s)he does so using the same input as the orbital mouse camera,
now this isnt too much of a problem, if the character is moving we can use the mouse-input to dictate the charaters rotation on a "up" axis, and if the
character is standing still we can use the mouse to dictate the camera rotation around the player, the question becomes. if the camera is offset by 90 degress,
while standing still, and we start to move, what should we do? the solution in _SomeRPG_ is that the player detectes rotation when standing still. but waits to apply
it to the player-modell until we start moving, so we will always begin to move the direction the camera is facing, now the problem arrises when we do our
swap from the orbital to the follow-camera once we start moving,

**the problem:**
when transitioning from the orbital camera to the following camera, i dont want the transition to be linear, as in if im offset by one 
unit to the left of the character, and im moving towards a offset of one unit behind the character, then every point along that transition 
should be one unit away from the player. a striaght line would "cut the corner" so to speak, and the center of this line would be closer to the player
then the two outer points, we need a curve to follow here. a shape where each point is equal distance from the center. now that is kinda wonky to calculate with
my current system, so my other option is to just snap from the orbital camera to the follow camera, and for a long time that is what i did, 
but there is a flimmer when you do this, a frame in the game that looks out of place. what is it that is wrong? well... you see when the camera snaps,
there is still a bitt of "latency" before the character model rotates, so that one frame that looks off is "between" the camera snap and the player rotation.

**the fix:**
im working on a solution here to rewrite how my cameras behave, hopefully this is the easy solution. My plan is to use that horizontal angle i mentioned in the
description of the orbital camera, and reduce it towards 0 when i swap my camera, to kindoff "swing" it back into place, unity has a built in AngleLerp which is pretty
neat for this kind off thing, im getting close to a solution that im liking, so we'll see what happens.

## Moving over to GitHub!

i've switched to hosting all my stuff on Github Pages, this means i might use this as an oportunity to share all of my projects here:
resource-files and all, i'll also gather my sideprojects here, in the meantime you can check out my socials!

[twitter](https://www.twitter.com/nyanDoggo) and [youtube](https://www.youtube.com/channel/UCJSZmbLX7AfLtouvXCySDow?view_as=subscriber)
