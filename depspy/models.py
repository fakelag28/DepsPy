from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field, RootModel

class Location(BaseModel):
    x: float
    y: float

class Level(BaseModel):
    level: int
    current_exp: int
    next_exp: int

class MapPOI(BaseModel):
    name: str
    city: str
    x: float
    y: float

class House(BaseModel):
    id: int
    location: Location
    name: str
    nearest_poi: MapPOI
    on_auction: bool

class Property(BaseModel):
    houses: List[House]
    businesses: List[dict]

class Money(BaseModel):
    bank: int
    hand: int
    deposit: int
    phone_balance: int
    donate_currency: int
    charity: Optional[Union[int, str]] = None
    total: int
    personal_accounts: Dict[str, str]

class Organization(BaseModel):
    name: str
    rank: str
    uniform: bool

class VIPInfo(BaseModel):
    level: Optional[str] = None
    add_vip: Union[str, int, None] = None
    expiration_date: Optional[int] = None

class Server(BaseModel):
    id: int
    name: str

class StatusInfo(BaseModel):
    online: bool
    player_id: int

class Admin(BaseModel):
    forum_url: str
    level: int
    nickname: str
    position: str
    short_name: str
    vk_url: str

class Player(BaseModel):
    id: int
    admin: Union[Admin, bool, None] = None
    drug_addiction: int
    health: int
    hours_played: int
    hunger: int
    job: Optional[str] = None
    law_abiding: int
    level: Level
    money: Money
    organization: Optional[Organization] = None
    phone_number: Optional[int] = None
    property: Property
    server: Server
    status: Union[StatusInfo, str, None] = None
    timestamp: int
    vip_info: Optional[VIPInfo] = None
    wanted_level: int
    warnings: int

class Interview(BaseModel):
    place: str
    time: str

class Interviews(BaseModel):
    data: Dict[str, Interview]
    timestamp: int

class OnlinePlayer(BaseModel):
    name: str
    level: Optional[int] = None
    member: Optional[str] = None
    position: Optional[str] = None
    inUniform: Optional[bool] = None
    isLeader: Optional[bool] = None
    isZam: Optional[bool] = None

class OnlinePlayers(BaseModel):
    data: Dict[str, OnlinePlayer]
    timestamp: int

class Fractions(BaseModel):
    data: List[str]
    timestamp: int

class Admins(BaseModel):
    admins: List[Admin]
    server: Server

class ServerStatus(BaseModel):
    has_online: Optional[bool]
    has_sobes: Optional[bool]
    last_update: Optional[int]

class Status(BaseModel):
    servers: Dict[str, ServerStatus]

class MapHouse(BaseModel):
    id: int
    lx: float
    ly: float
    name: str
    owner: Optional[str] = None
    hasAuction: Optional[bool] = None
    auMinBet: Optional[int] = None
    auTimeEnd: Optional[int] = None
    auStartPrice: Optional[int] = None
    nearest_poi: MapPOI

class MapBusiness(BaseModel):
    id: int
    lx: float
    ly: float
    name: str
    type: int
    owner: Optional[str] = None
    hasAuction: Optional[bool] = None
    auMinBet: Optional[int] = None
    auTimeEnd: Optional[int] = None
    auStartPrice: Optional[int] = None
    nearest_poi: MapPOI

class MapHouses(BaseModel):
    hasOwner: list[MapHouse]
    noOwner: list[MapHouse]
    onAuction: list[MapHouse]
    onMarketplace: list[MapHouse]

class MapBusinessesNoAuction(RootModel[dict[str, list[MapBusiness]]]):
    pass

class MapBusinesses(BaseModel):
    onAuction: list[MapBusiness]
    noAuction: MapBusinessesNoAuction
    onMarketplace: list[MapBusiness]

class MapResponse(BaseModel):
    houses: MapHouses
    businesses: MapBusinesses

class GhettoSquare(BaseModel):
    squareStart: Location
    squareEnd: Location
    color: int

class GhettoData(RootModel[dict[str, GhettoSquare]]):
    pass

class GhettoResponse(BaseModel):
    data: GhettoData
    timestamp: int 