from app.repository.repository_plane import PlaneRepository

from fastapi import APIRouter

router_planes = APIRouter(prefix='/planes', tags=['Самолеты'])




@router_planes.get('')
async def get_planes_all():
    planes = await PlaneRepository.get_all_plans()
    return {'planes': planes}


@router_planes.post('')
async def post_user():
    result = await PlaneRepository.post_planes()
    return {'messege': f'Добавлено новых самолетов: {result}'}