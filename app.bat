@REM GET RECT FROM POSE ESTIMATION
cd C:\Not So System Files\Study\6th sem\SGP Ideas\quick3D\lightweight-human-pose-estimation.pytorch
python find_rect.py -i "C:\Not So System Files\Study\6th sem\SGP Ideas\quick3D\src\images"


@REM RUN PIFU
cd "C:\Not So System Files\Study\6th sem\SGP Ideas\quick3D\src"
python -m apps.simple_test -r 256 --use_rect -i "C:\Not So System Files\Study\6th sem\SGP Ideas\quick3D\src\images"

@REM BACK TO REPO ROOT_PATH
cd "C:\Not So System Files\Study\6th sem\SGP Ideas\quick3D"