from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field
from datetime import datetime

class Location(BaseModel):
    x: float
    y: float

class Level(BaseModel):
    level: int
    current_exp: int
    next_exp: int

class Money(BaseModel):
    bank: int
    hand: int
    deposit: int
    phone_balance: int
    donate_currency: int
    charity: Optional[str]
    total: int
    personal_accounts: Dict[str, str]

class Organization(BaseModel):
    name: str
    rank: str
    uniform: bool
    last_seen: datetime

class Property(BaseModel):
    houses: List[Dict[str, Union[int, str, Location, bool]]]
    businesses: List[Dict[str, Union[int, str, Location, bool, int]]]

class VIPInfo(BaseModel):
    level: str
    add_vip: int
    expiration_date: int

class Server(BaseModel):
    id: int
    name: str

class Player(BaseModel):
    id: int
    admin: bool
    drug_addiction: int
    health: int
    hours_played: int
    hunger: int
    job: str
    last_seen: Optional[int]
    law_abiding: int
    level: Level
    money: Money
    organization: Optional[Organization]
    phone_number: int
    property: Property
    server: Server
    spouse: Optional[str]
    status: str
    timestamp: int
    vip_info: VIPInfo
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
    level: int
    member: Optional[str]
    position: Optional[str]
    inUniform: Optional[bool]
    isLeader: Optional[bool]
    isZam: Optional[bool]

class OnlinePlayers(BaseModel):
    data: Dict[str, OnlinePlayer]
    timestamp: int

class Fractions(BaseModel):
    data: List[str]
    timestamp: int

class Admin(BaseModel):
    nickname: str
    level: int
    position: str
    short_name: str
    forum_url: str
    vk_url: str

class Admins(BaseModel):
    admins: List[Admin]
    server: Server

class ServerStatus(BaseModel):
    has_online: Optional[bool]
    has_sobes: Optional[bool]
    last_update: Optional[int]

class Status(BaseModel):
    servers: Dict[str, ServerStatus]

class MapPOI(BaseModel):
    name: str
    city: str
    x: float
    y: float

class MapHouse(BaseModel):
    id: int
    lx: float
    ly: float
    name: str
    owner: str
    hasAuction: int
    auMinBet: int
    auTimeEnd: int
    auStartPrice: int
    nearest_poi: MapPOI

class MapBusiness(BaseModel):
    id: int
    lx: float
    ly: float
    name: str
    type: int
    owner: str
    hasAuction: int
    auMinBet: int
    auTimeEnd: int
    auStartPrice: int
    nearest_poi: MapPOI

class MapHouses(BaseModel):
    hasOwner: list[MapHouse]
    noOwner: list[MapHouse]
    onAuction: list[MapHouse]
    onMarketplace: list[MapHouse]

class MapBusinessesNoAuction(BaseModel):
    __root__: dict[str, list[MapBusiness]]

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

class GhettoData(BaseModel):
    __root__: dict[str, GhettoSquare]

class GhettoResponse(BaseModel):
    data: GhettoData 