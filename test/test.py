# -*- coding: utf-8 -*-

tests = {}

tests['t'] = u'{{SCnLStatement|1| \n\
                    {{SCnLUniversal|1}} {{SCnLVar|_t}} {{SCnLThereIs|1}}\n\
                        {{SCnLevel|1}} {{SCnLImplication|1}} \n\
                            {{SCnLevel|2}} {{SCnLIf|2}} \n\
                                {{SCnLAtomicExist| \n\
                                    {{SCnLVar|_t}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Треугольник|треугольник]]}} \n\
                                }} \n\
                            {{SCnLevel|2}} {{SCnLThen|2}} \n\
                                {{SCnLExistential|2}} {{SCnLVar|_a}}, {{SCnLVar|_b}}, {{SCnLVar|_c}}, {{SCnLVar|_o}} {{SCnLExistentialPropPref|2}} \n\
                                        {{SCnLevel|3}} {{SCnLAtomicExist| \n\
                                            {{SCnLVar|_a}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Отрезок|отрезок]]}} ;\n\
                                            {{SCnLVar|_a}} {{SCn_непринадлежность}} {{SCnLConcept|[[Геометрия:Отрезок|отрезок]]}} ;\n\
                                            {{SCnLVar|_a}} {{SCn_не_равно}} {{SCnLConcept|[[Геометрия:Отрезок|отрезок]]}} ;\n\
                                            {{SCnLVar|_a}} {{SCn_равно}} {{SCnLConcept|[[Геометрия:Отрезок|отрезок]]}} ;\n\
                                            {{SCnLVar|_a}} {{SCn_подмножество}} {{SCnLConcept|[[Геометрия:Отрезок|отрезок]]}} ;\n\
                                            {{SCnLVar|_a}} {{SCn_надмножество}} {{SCnLConcept|[[Геометрия:Отрезок|отрезок]]}} ;\n\
                                            {{SCnLVar|_a}} {{SCn_строгое_подмножество}} {{SCnLConcept|[[Геометрия:Отрезок|отрезок]]}} ;\n\
                                            {{SCnLVar|_a}} {{SCn_строгое_надмножество}} {{SCnLConcept|[[Геометрия:Отрезок|отрезок]]}} ;\n\
                                            {{SCnLOSet| {{SCnLVar|_t}}, {{SCnLVar|_a}} }} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Биссектриса|биссектриса*]]}} ;\n\
                                            {{SCnLVar|_b}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Отрезок|отрезок]]}} ;\n\
                                            {{SCnLOSet| {{SCnLVar|_t}}, {{SCnLVar|_b}} }} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Биссектриса|биссектриса*]]}} ;\n\
                                            {{SCnLVar|_c}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Окружность|окружность]]}} ;\n\
                                            {{SCnLOSet| {{SCnLVar|_t}}, {{SCnLVar|_c}} }} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Вписанность|вписанность*]]}} ;\n\
                                            {{SCnLVar|_o}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Геометрическая точка|геометрическая точка]]}} ;\n\
                                            {{SCnLOSet| {{SCnLVar|_c}}, {{SCnLVar|_o}} }} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Центр|центр*]]}} ;\n\
                                            {{SCnLOSet| {{SCnLSet| {{SCnLVar|_a}}, {{SCnLVar|_b}} }}, {{SCnLSet|{{SCnLVar|_o}} }} }} {{SCn_принадлежность}} {{SCnLConcept|[[Теория множеств:Пересечение|пересечение*]]}} \n\
                                            {{SCnLevel|2}} {{SCnLVar|a}} {{SCn_пересечение}} {{SCnLVar|b}} {{SCn_равно}} {{SCnLConcept|pc}}; \n\
                                            {{SCnLevel|2}} {{SCnLVar|a}} {{SCn_пересечение}} {{SCnLVar|c}} {{SCn_не_равно}} {{SCnLConcept|pc}}; \n\
                                            {{SCnLevel|2}} {{SCnLVar|a}} {{SCn_объединение}} {{SCnLVar|b}} {{SCn_равно}} {{SCnLConcept|pc}}; \n\
                                            {{SCnLevel|2}} {{SCnLVar|a}} {{SCn_объединение}} {{SCnLVar|c}} {{SCn_не_равно}} {{SCnLConcept|pc}}; \n\
                                        }} \n\
                .|cont}}'
                
tests['t0'] = u'{{SCnLStatement|1| \n\
                    {{SCnLUniversal|1}} {{SCnLVar|_t}} {{SCnLThereIs|1}}\n\
                        {{SCnLevel|1}} {{SCnLImplication|1}} \n\
                            {{SCnLevel|2}} {{SCnLIf|2}} \n\
                                {{SCnLAtomicExist| \n\
                                    {{SCnLVar|_t}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Треугольник|треугольник]]}} \n\
                                }} \n\
                            {{SCnLevel|2}} {{SCnLThen|2}} \n\
                                {{SCnLExistential|2}} {{SCnLVar|_a}}, {{SCnLVar|_b}}, {{SCnLVar|_c}}, {{SCnLVar|_o}} {{SCnLExistentialPropPref|2}} \n\
                                        {{SCnLevel|3}} {{SCnLAtomicExist| \n\
                                            {{SCnLVar|_a}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Отрезок|отрезок]]}} ;\n\
                                            {{SCnLevel|2}} {{SCnLOSet| {{SCnLVar|_t}}, {{SCnLVar|_a}} }} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Биссектриса|биссектриса*]]}} ;\n\
                                            {{SCnLevel|2}} {{SCnLVar|_b}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Отрезок|отрезок]]}} ;\n\
                                            {{SCnLevel|2}} {{SCnLOSet| {{SCnLVar|_t}}, {{SCnLVar|_b}} }} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Биссектриса|биссектриса*]]}} ;\n\
                                            {{SCnLevel|2}} {{SCnLVar|_c}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Окружность|окружность]]}} ;\n\
                                            {{SCnLevel|2}} {{SCnLOSet| {{SCnLVar|_t}}, {{SCnLVar|_c}} }} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Вписанность|вписанность*]]}} ;\n\
                                            {{SCnLevel|2}} {{SCnLVar|_o}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Геометрическая точка|геометрическая точка]]}} ;\n\
                                            {{SCnLevel|2}} {{SCnLOSet| {{SCnLVar|_c}}, {{SCnLVar|_o}} }} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Центр|центр*]]}} ;\n\
                                            {{SCnLevel|2}} {{SCnLOSet| {{SCnLSet| {{SCnLVar|_a}}, {{SCnLVar|_b}}}}, {{SCnLSet|{{SCnLVar|_o}}}}}} {{SCn_принадлежность}} {{SCnLConcept|[[Теория множеств:Пересечение|пересечение*]]}} \n\
                                        }} \n\
                .|cont}}'
                
tests['t1'] = u'{{SCnLStatement|1| \n\
                    {{SCnLUniversal|1}} {{SCnLVar|_ti}}, {{SCnLVar|_tj}}, {{SCnLVar|_tk}} {{SCnLThereIs|1}} \n\
                        {{SCnLevel|1}} {{SCnLImplication|1}} \n\
                            {{SCnLevel|2|{{SCn_перечисление|1}}}} {{SCnLIf|1}} \n\
                                {{SCnLAtomicExist| \n\
                                    {{SCnLSet| {{SCnLVar|_ti}}, {{SCnLVar|_tj}}, {{SCnLVar|_tk}}}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Непрямолинейная тройка точек|непрямолинейная тройка точек]]}} \n\
                                }}; \n\
                            {{SCnLevel|2|{{SCn_перечисление|1}}}} {{SCnLThen|1}} \n\
                                {{SCnLExistential|1}} {{SCnLVar| {{SCnLTex|\\alpha}}}} {{SCnLExistentialPropPref|1}} \n\
                                    {{SCnLevel|2}} {{SCnLConjunction|1}} \n\
                                        {{SCnLevel|3|{{SCn_перечисление|2}}}} {{SCnLAtomicExist| \n\
                                            {{SCnLVar| {{SCnLTex|\\alpha}}}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Плоскость|плоскость]]}}; \n\
                                            {{SCnLevel|3}} {{SCnLVar|_ti}} {{SCn_принадлежность}} {{SCnLVar|{{SCnLTex|\\alpha}}}}; \n\
                                            {{SCnLevel|3}} {{SCnLVar|_tj}} {{SCn_принадлежность}} {{SCnLVar|{{SCnLTex|\\alpha}}}}; \n\
                                            {{SCnLevel|3}} {{SCnLVar|_tk}} {{SCn_принадлежность}} {{SCnLVar|{{SCnLTex|\\alpha}}}} \n\
                                        }}; \n\
                                        {{SCnLevel|3|{{SCn_перечисление|2}}}} {{SCnLUniversal|1}} {{SCnLVar| {{SCnLTex|\\beta}}}} {{SCnLThereIs|1}} \n\
                                            {{SCnLevel|3}} {{SCnLImplication|1}} \n\
                                                {{SCnLevel|4|{{SCn_перечисление|3}}}} {{SCnLIf|1}} \n\
                                                    {{SCnLAtomicExist| \n\
                                                        {{SCnLVar| {{SCnLTex|\\beta}}}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Плоскость|плоскость]]}}, \n\
                                                        {{SCnLVar|_ti}} {{SCn_принадлежность}} {{SCnLVar| {{SCnLTex|\\beta}}}}, \n\
                                                        {{SCnLVar|_tj}} {{SCn_принадлежность}} {{SCnLVar| {{SCnLTex|\\beta}}}}, \n\
                                                        {{SCnLVar|_tk}} {{SCn_принадлежность}} {{SCnLVar| {{SCnLTex|\\beta}}}} \n\
                                                    }}; \n\
                                                {{SCnLevel|4|{{SCn_перечисление|3}}}} {{SCnLThen|1}} \n\
                                                    {{SCnLAtomicExist| \n\
                                                        {{SCnLSet| {{SCnLVar| {{SCnLTex|\\alpha}}}}, {{SCnLVar| {{SCnLTex|\\beta}}}} }} {{SCn_принадлежность}} {{SCnLConcept|совпадение*}} \n\
                                                    }} \n\
                .|cont }}'

tests['t2'] = u'{{SCnLStatement|1| \n\
                    {{SCnLUniversal|1}} {{SCnLVar|_ti}}, {{SCnLVar|_tj}}, {{SCnLVar|_tk}} \n\
                        {{SCnLevel|3|{{SCn_перечисление|2}}}} {{SCnLAtomicExist| \n\
                            {{SCnLVar| {{SCnLTex|\\alpha}}}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Плоскость|плоскость]]}}; \n\
                            {{SCnLevel|3}} {{SCnLVar|_ti}} {{SCn_принадлежность}} {{SCnLVar|{{SCnLTex|\\alpha}}}}; \n\
                            {{SCnLevel|3}} {{SCnLVar|_tj}} {{SCn_принадлежность}} {{SCnLVar|{{SCnLTex|\\alpha}}}}; \n\
                            {{SCnLevel|3}} {{SCnLVar|_tk}} {{SCn_принадлежность}} {{SCnLVar|{{SCnLTex|\\alpha}}}} \n\
                        }}; \n\
                .|cont }}'
                
tests['t3'] = u'{{SCnLStatement|1| \n\
                    {{SCnLUniversal|1}} {{SCnLVar|{{SCnLTex|\\mathbb E}}}} {{SCnLThereIs|1}} \n\
                        {{SCnLevel|1}} {{SCnLImplication|1}} \n\
                            {{SCnLevel|2|{{SCn_перечисление|1}}}} {{SCnLIf|1}} \n\
                                {{SCnLExistential|1}} {{SCnLVar|{{SCnLTex|\\alpha}}}} {{SCnLExistentialPropPref|1}} \n\
                                    {{SCnLevel|2}} {{SCnLAtomicExist| \n\
                                        {{SCnLVar|{{SCnLTex|\\mathbb E}}}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Пространство|пространство]]}}, \n\
                                        {{SCnLVar|{{SCnLTex|\\alpha}}}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Плоскость|плоскость]]}}, \n\
                                        {{SCnLVar|{{SCnLTex|\\alpha}}}} {{SCn_строгое_надмножество}} {{SCnLVar|{{SCnLTex|\\mathbb E}}}} \n\
                                    }}; \n\
                            {{SCnLevel|2|{{SCn_перечисление|1}}}} {{SCnLThen|1}} \n\
                                {{SCnLExistential|1}} {{SCnLVar|sp}}, {{SCnLVar|sk}} {{SCnLExistentialPropPref|1}} {{SCnLThereIs|1}}\n\
                                    {{SCnLevel|2}} {{SCnLConjunction|1}} \n\
                                        {{SCnLevel|3|{{SCn_перечисление|2}}}} {{SCnLAtomicExist| \n\
                                            {{SCnLVar|_sp}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Полупространство|полупространство]]}}, \n\
                                            {{SCnLVar|sk}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Полупространство|полупространство]]}}; \n\
                                            {{SCnLevel|3}} {{SCnLSet| {{SCnLVar|sp}}, {{SCnLVar|sk}} }} {{SCn_непринадлежность}} {{SCnLConcept|совпадение*}}; \n\
                                            {{SCnLevel|3}} {{SCnLVar|sp}} {{SCn_строгое_надмножество}} {{SCnLVar|{{SCnLTex|\\mathbb E}}}}, \n\
                                            {{SCnLVar|sk}} {{SCn_строгое_надмножество}} {{SCnLVar|{{SCnLTex|\\mathbb E}}}}; \n\
                                            {{SCnLevel|3}} {{SCnLOSet| {{SCnLVar|sp}}, {{SCnLVar|{{SCnLTex|\\alpha}}}} }} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Граница|граница*]]}},\n\
                                            {{SCnLOSet| {{SCnLVar|sk}}, {{SCnLVar|{{SCnLTex|\\alpha}}}} }} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Граница|граница*]]}} \n\
                                        }}; \n\
                                        {{SCnLevel|3|{{SCn_перечисление|2}}}} {{SCnLExistential|1}} {{SCnLVar|tk}}, {{SCnLVar|tp}}, {{SCnLVar|tm}}, {{SCnLVar|oh}}, {{SCnLVar|_ok}} {{SCnLExistentialPropPref|1}} {{SCnLThereIs|1}}\n\
                                            {{SCnLevel|3}} {{SCnLAtomicExist| \n\
                                                {{SCnLVar|_tk}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Геометрическая точка|геометрическая точка]]}}, \n\
                                                {{SCnLVar|_tp}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Геометрическая точка|геометрическая точка]]}}, \n\
                                                {{SCnLVar|_tm}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Геометрическая точка|геометрическая точка]]}}, \n\
                                                {{SCnLevel|3}} {{SCnLVar|_oh}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Отрезок|отрезок]]}}, \n\
                                                {{SCnLVar|_ok}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Отрезок|отрезок]]}};\n\
                                                {{SCnLevel|3}} {{SCnLOSet| {{SCnLVar|oh}}, {{SCnLVar|tk}} }} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Граничная точка|граничная точка*]]}}, \n\
                                                {{SCnLOSet| {{SCnLVar|oh}}, {{SCnLVar|tp}} }} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Граничная точка|граничная точка*]]}}; \n\
                                                {{SCnLevel|3}} {{SCnLOSet| {{SCnLVar|_ok}},{{SCnLVar|_tp}} }} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Граничная точка|граничная точка*]]}}, \n\
                                                {{SCnLOSet| {{SCnLVar|_ok}},{{SCnLVar|_tm}} }} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Граничная точка|граничная точка*]]}}; \n\
                                                {{SCnLevel|3}} {{SCnLSet| {{SCnLVar|{{SCnLTex|\\alpha}}}}, {{SCnLVar|_oh}} }} {{SCn_непринадлежность}} {{SCnLConcept|[[Язык множеств:Пересекающиеся|пересекающиеся множества*]]}}; \n\
                                                {{SCnLevel|3}} {{SCnLSet| {{SCnLVar|{{SCnLTex|\\alpha}}}},{{SCnLVar|_ok}} }} {{SCn_принадлежность}} {{SCnLConcept|[[Язык множеств:Пересекающиеся|пересекающиеся множества*]]}}; \n\
                                                {{SCnLevel|3}} {{SCnLVar|_tk}} {{SCn_принадлежность}} {{SCnLVar|_sp}},\n\
                                                {{SCnLVar|_tp}} {{SCn_принадлежность}} {{SCnLVar|_sp}}, \n\
                                                {{SCnLVar|_tm}} {{SCn_принадлежность}} {{SCnLVar|_sk}} \n\
                                            }} \n\
                .|cont}}'
                
tests['t4'] = u'{{SCnLStatement|1| \n\
                    {{SCnLUniversal|1}} {{SCnLVar|_ti}}, {{SCnLVar|_tj}}, {{SCnLVar|_tk}}, {{SCnLVar|{{SCnLTex|\\alpha}}}} \n\
                        {{SCnLevel|3|{{SCn_перечисление|2}}}} {{SCnLAtomicExist| \n\
                            {{SCnLVar| {{SCnLTex|\\alpha}}}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Плоскость|плоскость]]}}; \n\
                            {{SCnLevel|3}} {{SCnLVar|_ti}} {{SCn_принадлежность}} {{SCnLVar|{{SCnLTex|\\alpha}}}}; \n\
                            {{SCnLevel|3}} {{SCnLVar|_tj}} {{SCn_принадлежность}} {{SCnLVar|{{SCnLTex|\\alpha}}}}; \n\
                            {{SCnLevel|3}} {{SCnLVar|_tk}} {{SCn_принадлежность}} {{SCnLVar|{{SCnLTex|\\alpha}}}} \n\
                        }}; \n\
                .|cont }}'

tests['t5'] = u'{{SCnLStatement|1| \n\
                    {{SCnLUniversal|1}} {{SCnLVar|_ti}}, {{SCnLVar|_tj}}, {{SCnLVar|_tk}} {{SCnLThereIs|1}} \n\
                        {{SCnLevel|1}} {{SCnLImplication|1}} \n\
                            {{SCnLevel|2|{{SCn_перечисление|1}}}} {{SCnLIf|1}} \n\
                                {{SCnLAtomicExist| \n\
                                    {{SCnLSet| {{SCnLVar|_ti}}, {{SCnLVar|_tj}}, {{SCnLVar|_tk}}}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Непрямолинейная тройка точек|непрямолинейная тройка точек]]}} \n\
                                }}; \n\
                            {{SCnLevel|2|{{SCn_перечисление|1}}}} {{SCnLThen|1}} \n\
                                {{SCnLExistential|1}} {{SCnLVar| {{SCnLTex|\\alpha}}}} {{SCnLExistentialPropPref|1}} \n\
                                        {{SCnLevel|2}} {{SCnLAtomicExist| \n\
                                            {{SCnLVar| {{SCnLTex|\\alpha}}}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Плоскость|плоскость]]}}; \n\
                                            {{SCnLevel|3}} {{SCnLVar|_ti}} {{SCn_принадлежность}} {{SCnLVar|{{SCnLTex|\\alpha}}}}; \n\
                                            {{SCnLevel|3}} {{SCnLVar|_tj}} {{SCn_принадлежность}} {{SCnLVar|{{SCnLTex|\\alpha}}}}; \n\
                                            {{SCnLevel|3}} {{SCnLVar|_tk}} {{SCn_принадлежность}} {{SCnLVar|{{SCnLTex|\\alpha}}}} \n\
                                        }}; \n\
                .|cont }}'
                
tests['t6'] = u'{{SCnLStatement|1| \n\
                    {{SCnLUniversal|1}} {{SCnLVar|_ti}}, {{SCnLVar|_tj}}, {{SCnLVar|_tk}} {{SCnLThereIs|1}} \n\
                        {{SCnLevel|1}} {{SCnLImplication|1}} \n\
                            {{SCnLevel|2|{{SCn_перечисление|1}}}} {{SCnLIf|1}} \n\
                                {{SCnLAtomicExist| \n\
                                    {{SCnLSet| {{SCnLVar|_ti}}, {{SCnLVar|_tj}}, {{SCnLVar|_tk}}}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Непрямолинейная тройка точек|непрямолинейная тройка точек]]}} \n\
                                }}; \n\
                            {{SCnLevel|2|{{SCn_перечисление|1}}}} {{SCnLThen|1}} \n\
                                {{SCnLUniversal|1}} {{SCnLVar| {{SCnLTex|\\alpha}}}} \n\
                                        {{SCnLevel|2}} {{SCnLAtomicExist| \n\
                                            {{SCnLVar| {{SCnLTex|\\alpha}}}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Плоскость|плоскость]]}}; \n\
                                            {{SCnLevel|3}} {{SCnLVar|_ti}} {{SCn_принадлежность}} {{SCnLVar|{{SCnLTex|\\alpha}}}}; \n\
                                            {{SCnLevel|3}} {{SCnLVar|_tj}} {{SCn_принадлежность}} {{SCnLVar|{{SCnLTex|\\alpha}}}}; \n\
                                            {{SCnLevel|3}} {{SCnLVar|_tk}} {{SCn_принадлежность}} {{SCnLVar|{{SCnLTex|\\alpha}}}} \n\
                                        }}; \n\
                .|cont }}'

tests['t7'] = u'{{SCnLStatement|1| \n\
                    {{SCnLUniversal|1}} {{SCnLVar|{{SCnLTex|\\mathbb E}}}} {{SCnLThereIs|1}} \n\
                        {{SCnLevel|1}} {{SCnLImplication|1}} \n\
                            {{SCnLevel|2|{{SCn_перечисление|1}}}} {{SCnLIf|1}} \n\
                                {{SCnLExistential|1}} {{SCnLVar|{{SCnLTex|\\alpha}}}} {{SCnLExistentialPropPref|1}} \n\
                                    {{SCnLevel|2}} {{SCnLAtomicExist| \n\
                                        {{SCnLVar|{{SCnLTex|\\mathbb E}}}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Пространство|пространство]]}}, \n\
                                        {{SCnLVar|{{SCnLTex|\\alpha}}}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Плоскость|плоскость]]}}, \n\
                                        {{SCnLVar|{{SCnLTex|\\alpha}}}} {{SCn_строгое_надмножество}} {{SCnLVar|{{SCnLTex|\\mathbb E}}}} \n\
                                    }}; \n\
                            {{SCnLevel|2|{{SCn_перечисление|1}}}} {{SCnLThen|1}} \n\
                                {{SCnLExistential|1}} {{SCnLVar|sp}}, {{SCnLVar|sk}} {{SCnLExistentialPropPref|1}} {{SCnLThereIs|1}}\n\
                                    {{SCnLevel|2}} {{SCnLConjunction|1}} \n\
                                        {{SCnLevel|2}} {{SCnLConjunction|1}} \n\
                                            {{SCnLevel|3|{{SCn_перечисление|2}}}} {{SCnLAtomicExist| \n\
                                                {{SCnLVar|_sp}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Полупространство|полупространство]]}}, \n\
                                            }}; \n\
                                            {{SCnLevel|3|{{SCn_перечисление|2}}}} {{SCnLExistential|1}} {{SCnLVar|tk}}, {{SCnLVar|tp}}, {{SCnLVar|tm}}, {{SCnLVar|oh}}, {{SCnLVar|_ok}} {{SCnLExistentialPropPref|1}} {{SCnLThereIs|1}}\n\
                                                {{SCnLevel|3}} {{SCnLAtomicExist| \n\
                                                    {{SCnLVar|_tk}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Геометрическая точка|геометрическая точка]]}}, \n\
                                                }} \n\
                                        {{SCnLevel|3}} {{SCnLDisjunction|1}} \n\
                                            {{SCnLevel|3|{{SCn_перечисление|2}}}} {{SCnLAtomicExist| \n\
                                                {{SCnLVar|_sp}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Полупространство|полупространство]]}}, \n\
                                            }}; \n\
                                            {{SCnLevel|3|{{SCn_перечисление|2}}}} {{SCnLAtomicExist| \n\
                                                {{SCnLVar|_sp}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Полупространство|полупространство]]}}, \n\
                                            }}; \n\
                .|cont}}'
                
tests['t8'] = u'{{SCnLStatement|1| \n\
                    {{SCnLUniversal|1}} {{SCnLVar|{{SCnLTex|\\mathbb E}}}} {{SCnLThereIs|1}} \n\
                        {{SCnLevel|1}} {{SCnLImplication|1}} \n\
                            {{SCnLevel|2|{{SCn_перечисление|1}}}} {{SCnLIf|1}} \n\
                                {{SCnLExistential|1}} {{SCnLVar|{{SCnLTex|\\alpha}}}} {{SCnLExistentialPropPref|1}} \n\
                                    {{SCnLevel|2}} {{SCnLAtomicExist| \n\
                                        {{SCnLVar|{{SCnLTex|\\mathbb E}}}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Пространство|пространство]]}}, \n\
                                        {{SCnLVar|{{SCnLTex|\\alpha}}}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Плоскость|плоскость]]}}, \n\
                                        {{SCnLVar|{{SCnLTex|\\alpha}}}} {{SCn_строгое_надмножество}} {{SCnLVar|{{SCnLTex|\\mathbb E}}}} \n\
                                    }}; \n\
                            {{SCnLevel|2|{{SCn_перечисление|1}}}} {{SCnLThen|1}} \n\
                                {{SCnLExistential|1}} {{SCnLVar|sp}}, {{SCnLVar|sk}} {{SCnLExistentialPropPref|1}} {{SCnLThereIs|1}}\n\
                                    {{SCnLevel|2}} {{SCnLConjunction|1}} \n\
                                        {{SCnLevel|3|{{SCn_перечисление|2}}}} {{SCnLAtomicExist| \n\
                                            {{SCnLVar|_sp}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Полупространство|полупространство]]}}, \n\
                                        }}; \n\
                                        {{SCnLevel|3|{{SCn_перечисление|2}}}} {{SCnLExistential|1}} {{SCnLVar|tk}}, {{SCnLVar|tp}}, {{SCnLVar|tm}}, {{SCnLVar|oh}}, {{SCnLVar|_ok}} {{SCnLExistentialPropPref|1}} {{SCnLThereIs|1}}\n\
                                            {{SCnLevel|3}} {{SCnLAtomicExist| \n\
                                                {{SCnLVar|_tk}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Геометрическая точка|геометрическая точка]]}}, \n\
                                            }} \n\
                                        {{SCnLevel|3}} {{SCnLDisjunction|1}} \n\
                                            {{SCnLevel|3|{{SCn_перечисление|2}}}} {{SCnLAtomicExist| \n\
                                                {{SCnLVar|_sp}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Полупространство|полупространство]]}}, \n\
                                            }}; \n\
                                            {{SCnLevel|3|{{SCn_перечисление|2}}}} {{SCnLAtomicExist| \n\
                                                {{SCnLVar|_sp}} {{SCn_принадлежность}} {{SCnLConcept|[[Геометрия:Полупространство|полупространство]]}}, \n\
                                            }}; \n\
                .|cont}}'

tests['t9'] = u'{{SCnLStatement|1| \n\
                    {{SCnLUniversal|1}} {{SCnLVar|sp}} {{SCnLThereIs|1}} \n\
                        {{SCnLevel|2}} {{SCnLConjunction|1}} \n\
                            {{SCnLevel|3}} {{SCnLConjunction|1}} \n\
                                {{SCnLevel|4|{{SCn_перечисление|2}}}} {{SCnLAtomicExist| \n\
                                    {{SCnLVar|_sp}} {{SCn_принадлежность}} {{SCnLConcept|ab1}}, \n\
                                }}; \n\
                                {{SCnLevel|4|{{SCn_перечисление|2}}}} {{SCnLExistential|1}} {{SCnLVar|tk}} {{SCnLExistentialPropPref|1}} {{SCnLThereIs|1}}\n\
                                    {{SCnLevel|3}} {{SCnLAtomicExist| \n\
                                        {{SCnLVar|_tk}} {{SCn_принадлежность}} {{SCnLConcept|bhj}}, \n\
                                    }} \n\
                            {{SCnLevel|3}} {{SCnLDisjunction|1}} \n\
                                {{SCnLevel|4|{{SCn_перечисление|2}}}} {{SCnLAtomicExist| \n\
                                    {{SCnLVar|tk}} {{SCn_принадлежность}} {{SCnLConcept|mmmm}}, \n\
                                }}; \n\
                                {{SCnLevel|4|{{SCn_перечисление|2}}}} {{SCnLAtomicExist| \n\
                                    {{SCnLVar|tk}} {{SCn_принадлежность}} {{SCnLConcept|pppp}}, \n\
                                }}; \n\
                .|cont}}'