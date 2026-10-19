execute @a[scores={glider_time=1..}] ~ ~ ~ scoreboard players remove @s glider_time 1
execute @a[scores={glider_time=0}] ~ ~ ~ ability @s mayfly false
execute @a[scores={glider_time=0}] ~ ~ ~ tellraw @s {"rawtext":[{"text":"§cZbawood Glider: Flight expired."}]}
