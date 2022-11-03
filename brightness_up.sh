#!/usr/bin/env bash

value="$(cat /sys/class/backlight/amdgpu_bl0/brightness)"

if ((value < 240));
then
     	((value += 10))
fi

echo "$value"  > '/sys/class/backlight/amdgpu_bl0/brightness'
