from deficrawler.transformer import Transformer


class Mappers:

    @staticmethod
    def map_data(json_data, protocol, entity, attributes, transformations, query_elements):
        list_elements = []

        transformer = Transformer(
            entity=entity,
            protocol=protocol
        )

        for ele in json_data:
            element = {}
            for common_field, protocol_field in attributes.items():
                element[common_field] = (
                    transformer.transform(
                        element=ele,
                        common_field=common_field,
                        protocol_field=protocol_field,
                        transformations=transformations,
                        query_elements=query_elements
                    )
                )
                element['protocol'] = protocol
            list_elements.append(element)

        return list_elements
