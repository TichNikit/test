import logging

from app.repository.repository_plane import PlaneRepository

from fastapi import APIRouter

from app.schemas import PlanesIn

router_planes = APIRouter(prefix='/planes', tags=['Самолеты'])
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@router_planes.get('')
async def get_planes_all():
    planes = await PlaneRepository.get_all_planes()
    return {'planes': planes}


@router_planes.post('')
async def post_planes(planes: PlanesIn):
    result = await PlaneRepository.post_planes(planes.planes)
    logger.info(f'Добавлено новых самолетов: {result}')
    return {'message': f'Добавлено новых самолетов: {result}'}


@router_planes.delete('')
async def delete_planes():
    await PlaneRepository.delete_all_planes()
    logger.info('Все самолеты удалены из базы данных.')
    return {'message': 'Все самолеты успешно удалены из базы данных.'}
