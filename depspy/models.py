from typing import Dict, List, Optional, Union
from pydantic import BaseModel, Field

class Location(BaseModel):
    x: Optional[float] = None
    y: Optional[float] = None

class Level(BaseModel):
    level: Optional[int] = None
    current_exp: Optional[int] = None
    next_exp: Optional[int] = None

class MapPOI(BaseModel):
    name: Optional[str] = None
    city: Optional[str] = None
    x: Optional[float] = None
    y: Optional[float] = None

class House(BaseModel):
    id: Optional[int] = None
    location: Optional[Location] = None
    name: Optional[str] = None
    nearest_poi: Optional[MapPOI] = None
    on_auction: Optional[bool] = None

class Property(BaseModel):
    houses: List[House] = []
    businesses: List[dict] = []

class Money(BaseModel):
    bank: Optional[int] = None
    hand: Optional[int] = None
    deposit: Optional[int] = None
    phone_balance: Optional[int] = None
    donate_currency: Optional[int] = None
    charity: Optional[int] = None
    total: Optional[int] = None
    personal_accounts: Optional[Dict[str, str]] = None

class Organization(BaseModel):
    name: Optional[str] = None
    rank: Optional[str] = None
    uniform: Optional[bool] = None

class VIPInfo(BaseModel):
    level: Optional[str] = None
    add_vip: Optional[Union[str, int]] = None
    expiration_date: Optional[Union[int, str]] = None

class Server(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None

class StatusInfo(BaseModel):
    online: Optional[bool] = None
    player_id: Optional[int] = None

class Admin(BaseModel):
    forum_url: Optional[str] = None
    level: Optional[int] = None
    nickname: Optional[str] = None
    position: Optional[str] = None
    short_name: Optional[str] = None
    vk_url: Optional[str] = None

class PlayerFamilyMemberInfo(BaseModel):
    id: Optional[int] = None
    nickname: Optional[str] = None
    rank: Optional[int] = None
    leader: bool = False
    deputy: bool = False
    warns: Optional[int] = None

class PlayerFamilyInfo(BaseModel):
    id: int
    name: str
    timestamp: int
    member_info: PlayerFamilyMemberInfo

class Player(BaseModel):
    id: Optional[int] = None
    admin: Optional[Admin] = None
    drug_addiction: Optional[int] = None
    health: Optional[int] = None
    hours_played: Optional[int] = None
    hunger: Optional[int] = None
    job: Optional[str] = None
    law_abiding: Optional[int] = None
    level: Optional[Level] = None
    money: Optional[Money] = None
    organization: Optional[Organization] = None
    phone_number: Optional[int] = None
    property: Optional[Property] = None
    server: Optional[Server] = None
    status: Optional[StatusInfo] = None
    timestamp: Optional[int] = None
    vip_info: Optional[VIPInfo] = None
    wanted_level: Optional[int] = None
    warnings: Optional[int] = None
    family: Optional[PlayerFamilyInfo] = None

class Interview(BaseModel):
    place: Optional[str] = None
    time: Optional[str] = None

class Interviews(BaseModel):
    data: Optional[Dict[str, Interview]] = None
    timestamp: Optional[int] = None

class OnlinePlayer(BaseModel):
    name: Optional[str] = None
    level: Optional[int] = None
    member: Optional[str] = None
    position: Optional[str] = None
    inUniform: Optional[bool] = None
    isLeader: Optional[bool] = None
    isZam: Optional[bool] = None

class OnlinePlayers(BaseModel):
    data: Optional[Dict[str, OnlinePlayer]] = None
    timestamp: Optional[int] = None

class LeadersResponse(BaseModel):
    data: Optional[Dict[str, OnlinePlayer]] = None
    timestamp: Optional[int] = None

class SubleadersResponse(BaseModel):
    data: Optional[Dict[str, OnlinePlayer]] = None
    timestamp: Optional[int] = None

class Fractions(BaseModel):
    data: Optional[List[str]] = None
    timestamp: Optional[int] = None

class Admins(BaseModel):
    admins: List[Admin] = []
    server: Optional[Server] = None

class ServerStatus(BaseModel):
    has_online: Optional[bool] = None
    has_sobes: Optional[bool] = None
    last_update: Optional[int] = None

class Status(BaseModel):
    servers: Optional[Dict[str, ServerStatus]] = None

class MapHouse(BaseModel):
    id: Optional[int] = None
    lx: Optional[float] = None
    ly: Optional[float] = None
    name: Optional[str] = None
    owner: Optional[str] = None
    hasAuction: Optional[bool] = None
    auMinBet: Optional[int] = None
    auTimeEnd: Optional[int] = None
    auStartPrice: Optional[int] = None
    nearest_poi: Optional[MapPOI] = None

class MapBusiness(BaseModel):
    id: Optional[int] = None
    lx: Optional[float] = None
    ly: Optional[float] = None
    name: Optional[str] = None
    type: Optional[int] = None
    owner: Optional[str] = None
    hasAuction: Optional[bool] = None
    auMinBet: Optional[int] = None
    auTimeEnd: Optional[int] = None
    auStartPrice: Optional[int] = None
    nearest_poi: Optional[MapPOI] = None

class MapHouses(BaseModel):
    hasOwner: List[MapHouse] = []
    noOwner: List[MapHouse] = []
    onAuction: List[MapHouse] = []
    onMarketplace: List[MapHouse] = []

class MapBusinesses(BaseModel):
    onAuction: List[MapBusiness] = []
    noAuction: Optional[Dict[str, List[MapBusiness]]] = None
    onMarketplace: List[MapBusiness] = []

class MapResponse(BaseModel):
    houses: Optional[MapHouses] = None
    businesses: Optional[MapBusinesses] = None

class GhettoSquare(BaseModel):
    squareStart: Optional[Location] = None
    squareEnd: Optional[Location] = None
    color: Optional[int] = None

class GhettoData(BaseModel):
    data: Optional[Dict[str, GhettoSquare]] = None

class GhettoResponse(BaseModel):
    data: Optional[GhettoData] = None
    timestamp: Optional[int] = None

class FamilyMember(BaseModel):
    id: int
    nickname: str
    rank: Optional[int] = None
    player_id: Optional[int] = None
    warns: Optional[int] = None
    leader: bool = False
    deputy: bool = False
    joined_at: Optional[int] = None

class FamilyBase(BaseModel):
    id: int
    name: Optional[str] = None
    leader: Optional[str] = None
    level: Optional[int] = None
    flagId: Optional[int] = Field(None, alias="flagId")
    membersCount: Optional[int] = Field(0, alias="membersCount")

class Family(FamilyBase):
    members: List[FamilyMember] = []

class FamilyListResponse(BaseModel):
    families: List[FamilyBase] = []
    timestamp: int

class FamilyResponse(BaseModel):
    family: Family
    timestamp: int