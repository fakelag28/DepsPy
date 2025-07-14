from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field, RootModel

class Location(BaseModel):
    x: Optional[Union[float, str, None]] = None
    y: Optional[Union[float, str, None]] = None

class Level(BaseModel):
    level: Optional[Union[int, str, None]] = None
    current_exp: Optional[Union[int, str, None]] = None
    next_exp: Optional[Union[int, str, None]] = None

class MapPOI(BaseModel):
    name: Optional[Union[str, None]] = None
    city: Optional[Union[str, None]] = None
    x: Optional[Union[float, str, None]] = None
    y: Optional[Union[float, str, None]] = None

class House(BaseModel):
    id: Optional[Union[int, str, None]] = None
    location: Optional[Union[Location, str, None]] = None
    name: Optional[Union[str, None]] = None
    nearest_poi: Optional[Union[MapPOI, str, None]] = None
    on_auction: Optional[Union[bool, str, None]] = None

class Property(BaseModel):
    houses: Optional[Union[List[Union[House, str, None]], str, None]] = None
    businesses: Optional[Union[List[Union[dict, str, None]], str, None]] = None

class Money(BaseModel):
    bank: Optional[Union[int, str, None]] = None
    hand: Optional[Union[int, str, None]] = None
    deposit: Optional[Union[int, str, None]] = None
    phone_balance: Optional[Union[int, str, None]] = None
    donate_currency: Optional[Union[int, str, None]] = None
    charity: Optional[Union[int, str, None]] = None
    total: Optional[Union[int, str, None]] = None
    personal_accounts: Optional[Union[Dict[str, Union[str, None]], str, None]] = None

class Organization(BaseModel):
    name: Optional[Union[str, None]] = None
    rank: Optional[Union[str, None]] = None
    uniform: Optional[Union[bool, str, None]] = None

class VIPInfo(BaseModel):
    level: Optional[Union[str, None]] = None
    add_vip: Optional[Union[str, int, None]] = None
    expiration_date: Optional[Union[int, str, None]] = None

class Server(BaseModel):
    id: Optional[Union[int, str, None]] = None
    name: Optional[Union[str, None]] = None

class StatusInfo(BaseModel):
    online: Optional[Union[bool, str, None]] = None
    player_id: Optional[Union[int, str, None]] = None

class Admin(BaseModel):
    forum_url: Optional[Union[str, None]] = None
    level: Optional[Union[int, str, None]] = None
    nickname: Optional[Union[str, None]] = None
    position: Optional[Union[str, None]] = None
    short_name: Optional[Union[str, None]] = None
    vk_url: Optional[Union[str, None]] = None

class Player(BaseModel):
    id: Optional[Union[int, str, None]] = None
    admin: Optional[Union[Admin, bool, str, None]] = None
    drug_addiction: Optional[Union[int, str, None]] = None
    health: Optional[Union[int, str, None]] = None
    hours_played: Optional[Union[int, str, None]] = None
    hunger: Optional[Union[int, str, None]] = None
    job: Optional[Union[str, None]] = None
    law_abiding: Optional[Union[int, str, None]] = None
    level: Optional[Union[Level, str, None]] = None
    money: Optional[Union[Money, str, None]] = None
    organization: Optional[Union[Organization, str, None]] = None
    phone_number: Optional[Union[int, str, None]] = None
    property: Optional[Union[Property, str, None]] = None
    server: Optional[Union[Server, str, None]] = None
    status: Optional[Union[StatusInfo, str, None]] = None
    timestamp: Optional[Union[int, str, None]] = None
    vip_info: Optional[Union[VIPInfo, str, None]] = None
    wanted_level: Optional[Union[int, str, None]] = None
    warnings: Optional[Union[int, str, None]] = None

class Interview(BaseModel):
    place: Optional[Union[str, None]] = None
    time: Optional[Union[str, None]] = None

class Interviews(BaseModel):
    data: Optional[Union[Dict[str, Union[Interview, str, None]], str, None]] = None
    timestamp: Optional[Union[int, str, None]] = None

class OnlinePlayer(BaseModel):
    name: Optional[Union[str, None]] = None
    level: Optional[Union[int, str, None]] = None
    member: Optional[Union[str, None]] = None
    position: Optional[Union[str, None]] = None
    inUniform: Optional[Union[bool, str, None]] = None
    isLeader: Optional[Union[bool, str, None]] = None
    isZam: Optional[Union[bool, str, None]] = None

class OnlinePlayers(BaseModel):
    data: Optional[Union[Dict[str, Union[OnlinePlayer, str, None]], str, None]] = None
    timestamp: Optional[Union[int, str, None]] = None

class Fractions(BaseModel):
    data: Optional[Union[List[Union[str, None]], str, None]] = None
    timestamp: Optional[Union[int, str, None]] = None

class Admins(BaseModel):
    admins: Optional[Union[List[Union[Admin, str, None]], str, None]] = None
    server: Optional[Union[Server, str, None]] = None

class ServerStatus(BaseModel):
    has_online: Optional[Union[bool, str, None]] = None
    has_sobes: Optional[Union[bool, str, None]] = None
    last_update: Optional[Union[int, str, None]] = None

class Status(BaseModel):
    servers: Optional[Union[Dict[str, Union[ServerStatus, str, None]], str, None]] = None

class MapHouse(BaseModel):
    id: Optional[Union[int, str, None]] = None
    lx: Optional[Union[float, str, None]] = None
    ly: Optional[Union[float, str, None]] = None
    name: Optional[Union[str, None]] = None
    owner: Optional[Union[str, None]] = None
    hasAuction: Optional[Union[bool, str, None]] = None
    auMinBet: Optional[Union[int, str, None]] = None
    auTimeEnd: Optional[Union[int, str, None]] = None
    auStartPrice: Optional[Union[int, str, None]] = None
    nearest_poi: Optional[Union[MapPOI, str, None]] = None

class MapBusiness(BaseModel):
    id: Optional[Union[int, str, None]] = None
    lx: Optional[Union[float, str, None]] = None
    ly: Optional[Union[float, str, None]] = None
    name: Optional[Union[str, None]] = None
    type: Optional[Union[int, str, None]] = None
    owner: Optional[Union[str, None]] = None
    hasAuction: Optional[Union[bool, str, None]] = None
    auMinBet: Optional[Union[int, str, None]] = None
    auTimeEnd: Optional[Union[int, str, None]] = None
    auStartPrice: Optional[Union[int, str, None]] = None
    nearest_poi: Optional[Union[MapPOI, str, None]] = None

class MapHouses(BaseModel):
    hasOwner: Optional[Union[List[Union[MapHouse, str, None]], str, None]] = None
    noOwner: Optional[Union[List[Union[MapHouse, str, None]], str, None]] = None
    onAuction: Optional[Union[List[Union[MapHouse, str, None]], str, None]] = None
    onMarketplace: Optional[Union[List[Union[MapHouse, str, None]], str, None]] = None

class MapBusinessesNoAuction(RootModel[Optional[Union[Dict[str, Union[List[Union[MapBusiness, str, None]], str, None]], str, None]]]):
    pass

class MapBusinesses(BaseModel):
    onAuction: Optional[Union[List[Union[MapBusiness, str, None]], str, None]] = None
    noAuction: Optional[Union[MapBusinessesNoAuction, str, None]] = None
    onMarketplace: Optional[Union[List[Union[MapBusiness, str, None]], str, None]] = None

class MapResponse(BaseModel):
    houses: Optional[Union[MapHouses, str, None]] = None
    businesses: Optional[Union[MapBusinesses, str, None]] = None

class GhettoSquare(BaseModel):
    squareStart: Optional[Union[Location, str, None]] = None
    squareEnd: Optional[Union[Location, str, None]] = None
    color: Optional[Union[int, str, None]] = None

class GhettoData(RootModel[Optional[Union[Dict[str, Union[GhettoSquare, str, None]], str, None]]]):
    pass

class GhettoResponse(BaseModel):
    data: Optional[Union[GhettoData, str, None]] = None
    timestamp: Optional[Union[int, str, None]] = None 